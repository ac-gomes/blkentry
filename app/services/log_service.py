from ..database.model_service import LogFile, LogDataWerehouse
from ..database.connection import async_local_session
from sqlalchemy.future import select

class LogService:
    async def create_log(file_name: str, target_table: str):
        async with async_local_session() as session:
            session.add(LogFile(file_name=file_name, target_table=target_table))
            await session.commit()


    async def log_list():
        async with async_local_session() as session:
            query_result = await session.execute(select(LogFile))
            return query_result.scalars().all()


class TableLogService:
    async def create_table_log(target_db: str, file_id: int):
        async with async_local_session() as session:
            session.add(LogDataWerehouse(target_db=target_db, file_id=file_id))
            await session.commit()