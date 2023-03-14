from typing import List

from fastapi import APIRouter, HTTPException

from ..schemas.log import (
    LogActivityInput, DefaultOutput, ErrorOutput, LogListOutput, DwTableLog
)
from ..services.log_service import LogService, TableLogService

log_router = APIRouter(prefix='/log', tags=['log'])


@log_router.post('/create', response_model= DefaultOutput, responses={400: {'model': ErrorOutput}})
async def create_activity(log_input: LogActivityInput):
    try:
        await LogService.create_log(file_name=log_input.file_name, target_db=log_input.target_db)
        return DefaultOutput(message='logged activity successfully!')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


@log_router.post('/create/tablelog', response_model= DefaultOutput, responses={400: {'model': ErrorOutput}})
async def log_data_wherehouse(table_log_input: DwTableLog):
    try:
        await TableLogService.create_table_log(file_id=table_log_input.file_id, table_name=table_log_input.table_name)
        return DefaultOutput(message='logged activity successfully!')
    except Exception as error:
        raise HTTPException(400, detail='logged activity successfully!')


@log_router.get('/list', response_model=List[LogListOutput], responses={400: {'model': ErrorOutput}})
async def list_log():
    try:
        return await LogService.log_list()
    except Exception as error:
        raise HTTPException(400, detail=str(error))