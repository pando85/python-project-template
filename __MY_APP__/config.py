import os


LOG_LEVEL: str = os.environ.get('LOG_LEVEL', 'INFO')

RABBIT_HOST: str = os.environ.get('RABBIT_HOST', 'localhost')
RABBIT_USER: str = os.environ.get('RABBIT_USER', 'test')
RABBIT_PASSWORD: str = os.environ.get('RABBIT_PASSWORD', 'test1234')
