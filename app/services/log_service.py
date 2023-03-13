from ..database.model_service import LogFile
from ..database.connection import async_local_session


class LogService:
    async def create_log(file_name: str, target_db: str):
        async with async_local_session() as session:
            session.add(LogFile(file_name=file_name,target_db=target_db)) #when remove the var run as null value
            await session.commit()