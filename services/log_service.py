from unit_of_work import UnitOfWork
from schemas.log_schema import LogCreate
from models.log import Log

class LogService():
    def __init__(self, uow: UnitOfWork):
        self._uow = uow
    
    def create(self, input:LogCreate) -> Log:
        # Check 5!!!!
        with self._uow:
            entity = self._uow.logs.create(input.client_id, input.message)
        
        return entity
    
    def get_last_20(self, client_id: int) -> list[Log]:
        entities = self._uow.logs.get(client_id, 20)
        return entities