



from typing import Optional


class DatabaseService:
    def __init__(self) -> None:
        self.database = {
        1: "Alice",
        2: "Bob",
        3: "Andrew"
    }


    def find_by_id(self, user_id: int) -> Optional[str]:
        return self.database.get(user_id)

