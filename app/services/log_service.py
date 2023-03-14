from ..database.model_service import LogFile, LogDataWerehouse
from ..database.connection import async_local_session
from sqlalchemy.future import select

class LogService:
    async def create_log(file_name: str, target_db: str):
        async with async_local_session() as session:
            session.add(LogFile(file_name=file_name, target_db=target_db))
            await session.commit()


    async def log_list():
        async with async_local_session() as session:
            result = await session.execute(select(LogFile))
            return result.scalars().all()


class TableLogService:
    async def create_table_log(table_name: str, file_id: int):
        async with async_local_session() as session:
            session.add(LogDataWerehouse(table_name=table_name, file_id=file_id))
            await session.commit()