import aiohttp.web

from __MY_APP__.ping import ping_handler


def get_app() -> aiohttp.web.Application:
    app = aiohttp.web.Application()
    app.add_routes([
        aiohttp.web.get('/ping', ping_handler),
    ])

    return app
