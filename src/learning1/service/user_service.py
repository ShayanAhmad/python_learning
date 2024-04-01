from typing import Optional
from ..repository.db_service import DatabaseService as db_service_alias

class UserService:

    def __init__(self) -> None:
        self.db_service = db_service_alias()

    def get_user_by_id(self, user_id: int) -> Optional[str]:
        return self.db_service.find_by_id(user_id=user_id)
