from os import getenv
from dotenv import load_dotenv, find_dotenv

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


load_dotenv(find_dotenv())
DATABASE_URL = getenv('DATABASE_URL')


engine = create_async_engine(DATABASE_URL)
async_local_session = sessionmaker(engine, class_=AsyncSession)

