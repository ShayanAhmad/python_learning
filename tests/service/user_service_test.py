

class TestUserService:

    def test_find_user_by_id(self, mock_user_service, mock_db_service):
        mock_db_service.find_by_id.return_value = "Hakuna"

        result = mock_user_service.get_user_by_id(user_id=1)

        assert result == "Hakuna"
