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
        assert api_con.get_user_name()[0] == 405

    @pytest.mark.delete_user
    def test_delete_without_name(self, api_con):
        """deleted user without name"""
        assert api_con.delete_user()[0] == 405

    @pytest.mark.update_user
    def test_update_without_name(self, api_con):
        """updated user without name"""
        assert api_con.update_user()[0] == 405


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

    @pytest.mark.delete_user
    def test_delete_user_by_name(self, add_one_user):
        """deleted user by name"""
        rez = add_one_user.delete_user('test')
        assert rez[0] == 200
        assert rez[1]['message'] == 'test'

    @pytest.mark.update_user
    def test_update_by_name(self, add_one_user, params):
        """updated user by name"""
        rez = add_one_user.update_user('test', params(id=100, email='test@test.ru'))
        assert rez[0] == 200
        assert rez[1]['message'] == '100'


class TestWrongParameters:
    """tests with wrong params"""
    @pytest.mark.create_user
    @pytest.mark.xfail
    def test_create_user_wrong_param(self, api_con, params):
        """created user by wrong-id"""
        rez = api_con.create_user(params(id="test"))
        assert rez[0] == 400
        assert rez[1]['message'] == 'bad input'

    @pytest.mark.create_user_with_list
    @pytest.mark.xfail
    def test_create_user_with_list_wrong_param(self, api_con, params):
        """created user with list params wrong-id"""
        rez = api_con.create_user_with_list(params(id="test"))
        assert rez[0] == 400
        assert rez[1]['message'] == 'bad input'

    @pytest.mark.get_user
    def test_get_user_by_wrong_name(self, add_one_user):
        """get user by wrong name"""
        rez = add_one_user.get_user_name('111')
        assert rez[0] == 404
        assert rez[1]['message'] == 'User not found'

    @pytest.mark.delete_user
    def test_delete_user_by_wrong_name(self, add_one_user):
        """deleted user by wrong name"""
        assert add_one_user.delete_user('test1')[0] == 404

    @pytest.mark.update_user
    @pytest.mark.xfail
    def test_update_by_wrong_name(self, add_one_user, params):
        """updated user by wrong name"""
        rez = add_one_user.update_user('test_user', params(id=100, email='test@test.ru'))
        assert rez[0] == 404
