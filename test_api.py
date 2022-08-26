"""tests for api """
import pytest


class TestNoParam:

    """tests with empty parameters"""

    @pytest.mark.create_user
    def test_create_user_without_param(self, api_con):
        """created user without params"""
        assert api_con.create_user()[0] == 415

    @pytest.mark.create_user_with_list
    def test_create_user_with_list_without_param(self, api_con):
        """created user with list without params"""
        assert api_con.create_user_with_list()[0] == 415

    @pytest.mark.get_user
    def test_get_user_without_name(self, api_con):
        """get user by wrong name"""
        rez = api_con.get_user_name()
        assert rez[0] == 404
        assert rez[1]['message'] == 'User not found'


class TestWithParam:

    """tests with parameters"""
    @pytest.mark.create_user
    def test_create_user_by_id(self, api_con, params):
        """created user by params id"""
        rez = api_con.create_user(params(id=1))
        assert rez[0] == 200
        assert rez[1]['message'] == '1'

    @pytest.mark.create_user_with_list
    def test_create_user_with_list_by_id(self, api_con, params):
        """created user with list params id"""
        rez = api_con.create_user_with_list(params(id=2))
        assert rez[0] == 200
        assert rez[1]['message'] == 'ok'

    @pytest.mark.get_user
    def test_get_user_by_name(self, add_one_user):
        """get user by name"""
        rez = add_one_user.get_user_name('test')
        assert rez[0] == 200
        assert rez[1]['username'] == 'test'


class TestWrongParameters:
    """tests with wrong params"""

    @pytest.mark.create_user
    @pytest.mark.xfail
    def test_create_user_wrong_param(self, api_con, params):
        """created user by id"""
        rez = api_con.create_user(params(id="test"))
        assert rez[0] == 400
        assert rez[1]['message'] == 'bad input'

    @pytest.mark.create_user_with_list
    @pytest.mark.xfail
    def test_create_user_with_list_wrong_param(self, api_con, params):
        """created user with list params id"""
        rez = api_con.create_user_with_list(params(id="test"))
        assert rez[0] == 400
        assert rez[1]['message'] == 'bad input'

    @pytest.mark.get_user
    def test_get_user_by_wrong_name(self, add_one_user):
        """get user by wrong name"""
        rez = add_one_user.get_user_name('111')
        assert rez[0] == 404
        assert rez[1]['message'] == 'User not found'
