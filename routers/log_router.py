from fastapi import APIRouter, status, Depends
from schemas.log_schema import LogCreate, LogRead
from services.log_service import LogService
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/logs", tags=["Logs"])

def get_service(db:Session = Depends(get_db)):
    return LogService(db)

@router.post("", response_model=LogRead, status_code=status.HTTP_201_CREATED)
async def create(input: LogCreate, service: LogService = Depends()):
    return service.create(input)

@router.get("", response_model=list[LogRead], status_code=status.HTTP_200_OK)
async def get( service: LogService = Depends()):
    return service.get_last_20()
