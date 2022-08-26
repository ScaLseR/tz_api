"""tests for api """
import pytest


class TestEmptyParams:
    """tests with empty parameters"""

    @pytest.mark.create_user
    def test_create_user_without_params(self, api_con):
        """created user without params"""
        assert api_con.create_user()[0] == 415


class TestWithParams:
    """tests with parameters"""

    @pytest.mark.create_user
    def test_create_user_by_id(self, api_con, params):
        """created user by id"""
        rez = api_con.create_user(params(id=1))
        assert rez[0] == 200
        assert rez[1]['message'] == '1'


class TestWithWrongParams:
    """tests with wrong params"""
    @pytest.mark.create_user
    def test_create_user_wrong_param(self, api_con, params):
        """created user by id"""
        rez = api_con.create_user(params(id='test'))
        print('rez====', rez)
        assert rez[0] == 400
        assert rez[1]['message'] == 'bad input'
