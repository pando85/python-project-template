import aiohttp.web
from typing import Awaitable, Callable

from __MY_APP__.handlers import auth_handler, create_user_handler
from __MY_APP__.ping import ping_handler


def get_app(setup_db: Callable[[aiohttp.web.Application], Awaitable[None]]
            ) -> aiohttp.web.Application:
    app = aiohttp.web.Application()
    app.on_startup.append(setup_db)
    app.add_routes([
        aiohttp.web.get('/ping', ping_handler),
        aiohttp.web.post('/auth', auth_handler),
        aiohttp.web.post('/user', create_user_handler),
    ])

    return app
