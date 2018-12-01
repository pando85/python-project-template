from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
import unittest

from __MY_APP__.app import get_app


class RoutesTests(AioHTTPTestCase):

    async def get_application(self):
        return get_app()

    @unittest_run_loop
    async def test_ping(self, url='/ping'):
        request = await self.client.request('GET', url)
        assert request.status == 200
        response = await request.json()
        assert response == 'pong'


if __name__ == '__main__':
    unittest.main()
