from aiohttp.web import Request, Response

from __MY_APP__.functools import compose
from __MY_APP__ import logger
from __MY_APP__ import response


async def ping_handler(request: Request) -> Response:
    return compose(
        logger.debug,
        response.return_response)('"pong"')
