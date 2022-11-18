from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data.config import *

# DB_USER="postgres"
# DB_PASS="1006dinamo"
# DB_NAME="urbantech"
# DB_HOST="localhost"
class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            database=DB_NAME
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        tg_id BIGINT NOT NULL UNIQUE, 
        name VARCHAR(255) NOT NULL,
        fullname varchar(255) NULL,
        location varchar(255) NULL,
        phone varchar(15) NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, tg_id, name):
        sql = "INSERT INTO Users (tg_id, name) VALUES($1, $2) returning *"
        return await self.execute(sql, tg_id, name, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)


    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_phone(self, phone, tg_id):
        sql = "UPDATE Users SET phone=$1 WHERE tg_id=$2"
        return await self.execute(sql, phone, tg_id, execute=True)


    async def update_user_location(self, location, tg_id):
        sql = "UPDATE Users SET location=$1 WHERE tg_id=$2"
        return await self.execute(sql, location, tg_id, execute=True)

    async def update_user_name(self, fullname, tg_id):
        sql = "UPDATE Users SET fullname=$1 WHERE tg_id=$2"
        return await self.execute(sql, fullname, tg_id, execute=True)




    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)
        
        
        
        
# import asyncio

async def test():
    db = Database()
    await db.create()

    # users = await db.select_all_users()

    # print(f"Barcha foydalanuvchilar: {users}")
    # await db.add_user(113513543, "jaloliddin")
    users =await  db.select_all_users()
    print(users)

# asyncio.run(test())
