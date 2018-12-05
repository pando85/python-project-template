from aiohttp.web import Request, Response, json_response
import passlib

from __MY_APP__.db import create_user, get_user
from __MY_APP__.user import User


async def auth_handler(request: Request) -> Response:
    pool = request.app['pool']
    user_request = User(**(await request.json()))

    async with pool.acquire() as connection:
        user_data = await get_user(connection, user_request.username)
    is_verified = passlib.hash.pbkdf2_sha256.verify(user_request.password, user_data.password)
    msg = {'verified': is_verified}
    return json_response(msg)


async def create_user_handler(request: Request) -> Response:
    pool = request.app['pool']
    user_request = User(**(await request.json()))

    async with pool.acquire() as connection:
        await create_user(connection, user_request)
    msg = {'status': 'created'}
    return json_response(msg)
