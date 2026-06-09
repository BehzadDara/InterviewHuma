from fastapi import APIRouter, status, Depends
from schemas.log_schema import LogCreate, LogRead
from services.log_service import LogService
from sqlalchemy.orm import Session
from database import get_db
from unit_of_work import UnitOfWork

router = APIRouter(prefix="/logs", tags=["Logs"])

def get_service(db:Session = Depends(get_db)):
    return LogService(UnitOfWork(db))

@router.post("", response_model=LogRead, status_code=status.HTTP_201_CREATED)
async def create(input: LogCreate, service: LogService = Depends(get_service)):
    return service.create(input)

@router.get("/{client_id}", response_model=list[LogRead], status_code=status.HTTP_200_OK)
async def get(client_id:int, service: LogService = Depends(get_service)):
    return service.get_last_20(client_id)
