import aiohttp
import asyncpg
import passlib.hash

from __MY_APP__.config import (ADMIN_USER, ADMIN_PASSWORD, POSTGRES_HOST, POSTGRES_PORT,
                               POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD)
from __MY_APP__ import logger
from __MY_APP__.user import User

USERS_TABLE_NAME = 'users'


async def check_table_exists(conn: asyncpg.connect, table: str) -> bool:
    r = await conn.fetchrow(f'''
        SELECT EXISTS (
            SELECT 1
            FROM   pg_tables
            WHERE  schemaname = 'public'
            AND    tablename = $1
            );
    ''', table)
    return r['exists']


async def create_user(conn: asyncpg.connect, user: User) -> asyncpg.Record:
    await conn.execute(f'''
        INSERT INTO {USERS_TABLE_NAME}(username, password) VALUES($1, $2)
    ''', user.username, passlib.hash.pbkdf2_sha256.hash(user.password))


async def get_user(conn: asyncpg.connection, username: str) -> User:
    row = await conn.fetchrow(
        f'SELECT * FROM {USERS_TABLE_NAME} WHERE username = $1', username)
    return User(**dict(row))


async def init_db(conn: asyncpg.connect) -> None:
    if await check_table_exists(conn, USERS_TABLE_NAME):
        logger.info('Already initializated.')
        return

    logger.info(f'Create table: {USERS_TABLE_NAME}')
    await conn.execute(f'''
        CREATE TABLE {USERS_TABLE_NAME}(
            username text PRIMARY KEY,
            password text
        )
    ''')

    logger.info(f'Create admin user')
    await create_user(conn, User(ADMIN_USER, ADMIN_PASSWORD))


async def setup_db(app: aiohttp.web.Application) -> None:
    app['pool'] = await asyncpg.create_pool(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        database=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD)
    async with app['pool'].acquire() as connection:
        await init_db(connection)
