from sqlalchemy.orm import Session
from sqlalchemy import desc
from models.log import Log
from datetime import datetime

class LogRepository():
    def __init__(self, db:Session):
        self._db = db
    
    def create(self, client_id:int, message:str) -> Log:
        entity = Log(client_id=client_id, message=message, created_at=datetime.now)
        self._db.add(entity)
        self._db.flush()
        return entity
    
    def get(self, client_id:int, count:int) -> list[Log]:
         entities = (
            self._db.query(Log)
            .filter(Log.client_id == client_id)
            .order_by(desc(Log.created_at))
            .limit(count)
            .all()
            )
         return entities