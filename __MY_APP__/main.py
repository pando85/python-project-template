import aiohttp.web

from __MY_APP__.app import get_app
from __MY_APP__.db import setup_db
from __MY_APP__.logger import access_logger


def main():
    app = get_app(setup_db)
    aiohttp.web.run_app(app, access_log=access_logger)
