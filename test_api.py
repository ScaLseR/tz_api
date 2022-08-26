"""tests for api """
import pytest


class TestEmptyUsers:
    """tests with empty users in base"""

    def test_create_user_by_id(self, api_con, params):
        """create user by id"""
        rez = api_con.create_user(params(id=1))
        assert rez[0] == 200
        assert rez[1]['message'] == '1'

