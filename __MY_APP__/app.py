import aiohttp.web

from __MY_APP__.ping import ping_handler
from __MY_APP__.mq import init_rabbit_client


def get_app() -> aiohttp.web.Application:
    app = aiohttp.web.Application()
    app.on_startup.append(init_rabbit_client)
    app.add_routes([
        aiohttp.web.get('/ping', ping_handler),
    ])

    return app
