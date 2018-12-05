from aiohttp.web import Request, Response, json_response
import passlib

from __MY_APP__.db import create_user, get_user
from __MY_APP__.user import User, to_dict


async def auth_handler(request: Request) -> Response:
    pool = request.app['pool']
    user_request = User(**(await request.json()))

    async with pool.acquire() as connection:
        user_data = await get_user(connection, user_request.username)
    if not user_data:
        return json_response("'user does not exists'", status=422)
    is_verified = passlib.hash.pbkdf2_sha256.verify(user_request.password, user_data.password)
    if not is_verified:
        return json_response("'password does not match'", status=422)
    msg = {'verified': is_verified}
    return json_response(msg)


async def create_user_handler(request: Request) -> Response:
    pool = request.app['pool']
    user_request = User(**(await request.json()))

    async with pool.acquire() as connection:
        if await get_user(connection, user_request.username):
            return json_response("'user already exist'", status=409)
        await create_user(connection, user_request)
    msg = to_dict(user_request)
    return json_response(msg, status=201)
