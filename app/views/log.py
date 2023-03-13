from fastapi import APIRouter,HTTPException

from ..schemas.log import LogActivityInput, DefaultOutput
from ..services.log_service import LogService

log_router = APIRouter(prefix='/log')


@log_router.post('/create', response_model= DefaultOutput)
async def create_activity(activity_input: LogActivityInput):
    try:
        await LogService.create_log(file_name=activity_input.file_name, target_db= activity_input.target_db)
        return DefaultOutput('logged activity')
    except Exception as error:
        raise HTTPException(400, detail=str(error))