from sqlalchemy.orm import Session
from repositories.log_repository import LogRepository

class UnitOfWork():
    def __init__(self, db:Session):
        self._db = db
        self.logs = LogRepository(self._db)

    def __commit(self) -> None:
        self._db.commit()

    def __rollback(self) -> None:
        self._db.rollback()

    def __enter__(self) -> 'UnitOfWork':
        return self
    
    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            self.__commit()
        else:
            self.__rollback()