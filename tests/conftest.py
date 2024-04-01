from unittest import mock
import pytest

from src.learning1.service.user_service import UserService


@pytest.fixture
def mock_db_service():
    # so you need to use the instantiation of the database_service as used in the user_service.
    # key thing to remember here is that you shouldn't mock the original databaseService as that
    # will cause issues! 
    # You must always mock the things the way they are used from a testable class/method.
    with mock.patch("src.learning1.service.user_service.db_service_alias") as db_service:
        return db_service.return_value

@pytest.fixture
def mock_user_service(mock_db_service):
    user_service = UserService()
    user_service.db_service = mock_db_service
    return user_service
