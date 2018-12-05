import unittest

from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from __MY_APP__.app import get_app
from __MY_APP__.db import setup_db


class DBTests(AioHTTPTestCase):

    async def get_application(self):
        return get_app(setup_db)

    @unittest_run_loop
    async def test_get_user(self):
        pass


if __name__ == '__main__':
    unittest.main()
