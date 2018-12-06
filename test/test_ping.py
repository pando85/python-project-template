import pytest

from __MY_APP__.app import get_app
from __MY_APP__.db import setup_db


@pytest.fixture
def cli(loop, aiohttp_client):
    app = get_app(setup_db)
    return loop.run_until_complete(aiohttp_client(app))

    async def get_application(self):
        return get_app(setup_db)


async def test_auth(cli):
    resp = await cli.get('/ping')
    assert resp.status == 200
    assert await resp.json() == 'pong'
