import pytest

from __MY_APP__.app import get_app
from __MY_APP__.db import setup_db


@pytest.fixture
def cli(loop, aiohttp_client):
    app = get_app(setup_db)
    return loop.run_until_complete(aiohttp_client(app))


async def test_auth(cli):
    resp = await cli.post('/auth', json={'username': 'admin', 'password': 'admin'})
    assert resp.status == 200
    assert await resp.json() == {'token': 'TODO'}


async def test_auth_incorret_user(cli):
    resp = await cli.post('/auth', json={'username': 'foo', 'password': 'foo'})
    assert resp.status == 422
    assert await resp.json() == "'user does not exists'"


async def test_auth_incorret_password(cli):
    resp = await cli.post('/auth', json={'username': 'admin', 'password': 'foo'})
    assert resp.status == 422
    assert await resp.json() == "'password does not match'"


async def test_user(cli):
    user = {'username': 'test2', 'password': 'test1234'}
    resp = await cli.post('/user', json=user)
    assert resp.status == 201
    assert await resp.json() == user
