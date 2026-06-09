from unit_of_work import UnitOfWork
from schemas.log_schema import LogCreate
from models.log import Log
from exceptions.log_exception import RateLimitException

class LogService():
    def __init__(self, uow: UnitOfWork):
        self._uow = uow
    
    def create(self, input:LogCreate) -> Log:
        count_last_minute = self._uow.logs.count_last_minute(input.client_id)
        if count_last_minute > 5:
            raise RateLimitException('Client rate limit. Try after 1 minute')

        with self._uow:
            entity = self._uow.logs.create(input.client_id, input.message)
        
        return entity
    
    def get_last_20(self, client_id: int) -> list[Log]:
        entities = self._uow.logs.get(client_id, 20)
        return entities