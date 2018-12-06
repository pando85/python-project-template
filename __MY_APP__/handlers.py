from aiohttp.web import Request, Response, json_response

from __MY_APP__ import logger
from __MY_APP__.db import create_user
from __MY_APP__.functools import compose
from __MY_APP__.token import create_token
from __MY_APP__.typing import Maybe, Error, Success
from __MY_APP__.verify import check_password


async def auth_handler(request: Request) -> Response:
    return await compose(
        check_password,
        logger.debug,
        create_token,
        logger.debug,
        return_response
    )(request)


async def create_user_handler(request: Request) -> Response:
    return await compose(
        create_user,
        return_response
    )(request)


def return_response(r: Maybe[Success]) -> Response:
    if isinstance(r, Error):
        return json_response(r.msg, status=r.status_code)
    return json_response(r.json, status=r.status_code)
