import pytest
from unittest.mock import MagicMock
from services.log_service import LogService
from models.log import Log
from datetime import datetime
from schemas.log_schema import LogCreate

@pytest.fixture
def mock_repository():
    return MagicMock()

@pytest.fixture
def service(mock_repository):
    uow = MagicMock()
    uow.logs = mock_repository
    return LogService(uow)

def test_create_returns_log(service: LogService, mock_repository):
    mock_repository.create.return_value = Log(id=1, client_id=1, message='test', created_at=datetime.now())
    mock_repository.count_last_minute.return_value = 0

    entity = service.create(LogCreate(client_id=1, message='test'))

    assert entity.id == 1
    assert entity.client_id == 1
    assert entity.message == 'test'
    mock_repository.create.assert_called_once_with(1, 'test')