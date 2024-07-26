from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.sql import text
import asyncio

DATABASE_URL = "postgresql+asyncpg://user:password@db/db"

async def test_connection():
    engine = create_async_engine(DATABASE_URL, echo=True)
    async with engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        print(result.fetchall())

asyncio.run(test_connection())