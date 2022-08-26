"""tests for api """
import pytest
import allure


class TestNoParam:
    """tests with empty parameters"""

    @allure.feature("Create user /user")
    @allure.story('Создаем пользователя без указания обязательных параметров')
    @pytest.mark.create_user
    def test_create_user_without_param(self, api_con):
        """created user without params"""
        with allure.step("Создаем пользователя"):
            rez = api_con.create_user()
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 415"):
            assert rez[0] == 415, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Creates list of users /user/createWithList")
    @allure.story('Создаем список пользователей без указания обязательных параметров')
    @pytest.mark.create_user_with_list
    def test_create_user_with_list_without_param(self, api_con):
        """created user with list without params"""
        with allure.step("Создаем пользователя"):
            rez = api_con.create_user_with_list()
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 415"):
            assert rez[0] == 415, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Get user /user/{username}")
    @allure.story('Получаем пользователя без указания обязательного параметра username')
    @pytest.mark.get_user
    def test_get_user_without_name(self, api_con):
        """get user by wrong name"""
        with allure.step("Получаем пользователя"):
            rez = api_con.get_user_name()
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 405"):
            assert rez[0] == 405, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Delete user /user/{username}")
    @allure.story('Удаляем пользователя без указания обязательного параметра username')
    @pytest.mark.delete_user
    def test_delete_without_name(self, api_con):
        """deleted user without name"""
        with allure.step("Удаляем пользователя"):
            rez = api_con.delete_user()
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 405"):
            assert rez[0] == 405, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Updated user /user/{username}")
    @allure.story('Обновляем пользователя без указания обязательного параметра username')
    @pytest.mark.update_user
    def test_update_without_name(self, api_con):
        """updated user without name"""
        with allure.step("Обновляем пользователя"):
            rez = api_con.update_user()
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 405"):
            assert rez[0] == 405, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Login user into the system  /user/login")
    @allure.story('Выполняем вход пользователя без указания обязательного параметра username')
    @pytest.mark.login_user
    def test_login_user_without_name(self, api_con):
        """logged user without name"""
        password = '12345'
        with allure.step(f"Выполняем логин используя только параметр password = {password}"):
            rez = api_con.login_user(password=password)
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 400"):
            assert rez[0] == 400, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Login user into the system  /user/login")
    @allure.story('Выполняем вход пользователя без указания обязательного параметра password')
    @pytest.mark.login_user
    def test_login_user_without_password(self, api_con):
        """logged user without password"""
        name = 'test'
        with allure.step(f"Выполняем логин используя только параметр username = {name}"):
            rez = api_con.login_user(name=name)
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 400"):
            assert rez[0] == 400, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Login user into the system  /user/login")
    @allure.story('Выполняем вход пользователя без указания '
                  'обязательных параметров username, password')
    @pytest.mark.login_user
    def test_login_user_without_name_password(self, api_con):
        """logged user without password"""
        with allure.step("Выполняем логин без указания "
                         "обязательных параметров username, password"):
            rez = api_con.login_user()
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 400"):
            assert rez[0] == 400, f'Неверный код ответа, получен {rez[0]}'


class TestWithParam:
    """tests with parameters"""

    @allure.feature("Create user /user")
    @allure.story('Создаем пользователя с указанием корректных параметров')
    @pytest.mark.create_user
    def test_create_user_by_id(self, api_con, params):
        """created user by correct params id"""
        z_id = 1
        with allure.step(f"Создаем пользователя с id = {z_id}"):
            rez = api_con.create_user(params(id=z_id))
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 200"):
            assert rez[0] == 200, f'Неверный код ответа, получен {rez[0]}'
        with allure.step(f"Проверяем содержание поля message "
                         f"ответа {rez[1]['message']} == {z_id}"):
            assert rez[1]['message'] == str(z_id), \
                f'Неверное значение поля message, получен {rez[1]}'

    @allure.feature("Creates list of users /user/createWithList")
    @allure.story('Создаем список пользователей с указанием корректных параметров')
    @pytest.mark.create_user_with_list
    def test_create_user_with_list_by_id(self, api_con, params):
        """created user with correct list params id"""
        z_id = 2
        with allure.step(f"Создаем пользователя через список с id = {z_id}"):
            rez = api_con.create_user_with_list(params(id=z_id))
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 200"):
            assert rez[0] == 200, f'Неверный код ответа, получен {rez[0]}'
        with allure.step(f"Проверяем содержание поля message "
                         f"ответа {rez[1]['message']} == 'ok'"):
            assert rez[1]['message'] == 'ok', \
                f'Неверное значение поля message, получен {rez[1]}'

    @allure.feature("Get user /user/{username}")
    @allure.story('Получаем информацию о пользователе по корректному параметру username')
    @pytest.mark.get_user
    def test_get_user_by_name(self, add_one_user):
        """get user by correct name"""
        name = 'test'
        with allure.step(f"Получаем информацию о пользователе username = {name}"):
            rez = add_one_user.get_user_name(name)
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 200"):
            assert rez[0] == 200, f'Неверный код ответа, получен {rez[0]}'
        with allure.step("Проверяем содержание поля username ответа"):
            assert rez[1]['username'] == 'test', \
                f'Неверное значение поля username, получен {rez[1]}'

    @allure.feature("Delete user /user/{username}")
    @allure.story('Удаляем пользователя по корректному параметру username')
    @pytest.mark.delete_user
    def test_delete_user_by_name(self, add_one_user):
        """deleted user by correct name"""
        name = 'test'
        with allure.step(f"Удаляем пользователя username = {name}"):
            rez = add_one_user.delete_user(name)
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 200"):
            assert rez[0] == 200, f'Неверный код ответа, получен {rez[0]}'
        with allure.step(f"Проверяем содержание поля message "
                         f"ответа {rez[1]['message']} == {name}"):
            assert rez[1]['message'] == name, \
                f'Неверное значение поля message, получен {rez[1]}'

    @allure.feature("Updated user /user/{username}")
    @allure.story('Обновляем пользователя по корректному параметру username')
    @pytest.mark.update_user
    def test_update_by_name(self, add_one_user, params):
        """updated user by correct name"""
        name = 'test'
        z_id = 100
        email = 'test@test.ru'
        with allure.step(f"Обновляем информацию о пользователе "
                         f"username = {name}, id = {z_id}, email = {email}"):
            rez = add_one_user.update_user(name, params(id=z_id, email=email))
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 200"):
            assert rez[0] == 200, f'Неверный код ответа, получен {rez[0]}'
        with allure.step(f"Проверяем содержание поля message "
                         f"ответа {rez[1]['message']} == {str(z_id)}"):
            assert rez[1]['message'] == str(z_id), \
                f'Неверное значение поля message, получен {rez[1]}'

    @allure.feature("Login user into the system  /user/login")
    @allure.story('Выполняем вход пользователя по корректным параметрам username, password')
    @pytest.mark.login_user
    def test_login_user_by_name_password(self, add_one_user):
        """logged user by correct name and password"""
        name = 'test'
        password = '12345'
        with allure.step(f"Выполняем вход пользователя "
                         f"username = {name}, password = {password}"):
            rez = add_one_user.login_user(name=name, password=password)
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 200"):
            assert rez[0] == 200, f'Неверный код ответа, получен {rez[0]}'
        with allure.step(f"Проверяем содержание поля message ответа "
                         f"'logged in user session:' in {rez[1]['message']}"):
            assert 'logged in user session:' in rez[1]['message'], \
                f'Неверное значение поля message, получен {rez[1]}'

    @allure.feature("Logs out current logged users  /user/logout")
    @allure.story('Выполняем выход предварительно залогиненного пользователя')
    @pytest.mark.logout_user
    def test_logout_user(self, add_one_user):
        """logout user session"""
        name = 'test'
        password = '12345'
        with allure.step(f"Выполняем предварительный вход пользователя "
                         f"username = {name}, password = {password}"):
            _ = add_one_user.login_user(name=name, password=password)
        rez = add_one_user.logout_user()
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 200"):
            assert rez[0] == 200, f'Неверный код ответа, получен {rez[0]}'
        with allure.step("Проверяем содержание поля message ответа"):
            assert rez[1]['message'] == 'ok', \
                f'Неверное значение поля message, получен {rez[1]}'


class TestWrongParameters:
    """tests with wrong params"""

    @allure.feature("Create user /user")
    @allure.story('Создаем пользователя с некорректным id')
    @pytest.mark.create_user
    def test_create_user_wrong_param(self, api_con, params):
        """created user by wrong-id"""
        z_id = 'test'
        with allure.step(f"Создаем пользователя с id={z_id}"):
            rez = api_con.create_user(params(id=z_id))
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 400"):
            assert rez[0] == 400, f'Неверный код ответа, получен {rez[0]}'
        with allure.step(f"Проверяем содержание поля message ответа "
                         f"{rez[1]['message']} == 'bad input'"):
            assert rez[1]['message'] == 'bad input', \
                f'Неверное значение поля message, получен {rez[1]}'

    @allure.feature("Creates list of users /user/createWithList")
    @allure.story('Создаем пользователей списком с некорректным id')
    @pytest.mark.create_user_with_list
    def test_create_user_with_list_wrong_param(self, api_con, params):
        """created user with list params wrong-id"""
        z_id = 'test'
        with allure.step(f"Создаем пользователя с id={z_id}"):
            rez = api_con.create_user_with_list(params(id=z_id))
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 400"):
            assert rez[0] == 400, f'Неверный код ответа, получен {rez[0]}'
        with allure.step(f"Проверяем содержание поля message ответа "
                         f"{rez[1]['message']} == 'bad input'"):
            assert rez[1]['message'] == 'bad input', \
                f'Неверное значение поля message, получен {rez[1]}'

    @allure.feature("Get user /user/{username}")
    @allure.story('Получаем информацию о пользователе с некорректным username')
    @pytest.mark.get_user
    def test_get_user_by_wrong_name(self, add_one_user):
        """get user by wrong name"""
        name = '111'
        with allure.step(f"Получаем информацию о пользователе username={name}"):
            rez = add_one_user.get_user_name(name)
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 404"):
            assert rez[0] == 404, f'Неверный код ответа, получен {rez[0]}'
        with allure.step(f"Проверяем содержание поля message ответа "
                         f"{rez[1]['message']} == 'User not found'"):
            assert rez[1]['message'] == 'User not found', \
                f'Неверное значение поля message, получен {rez[1]}'

    @allure.feature("Delete user /user/{username}")
    @allure.story('Удаляяем пользователя с некорректным username')
    @pytest.mark.delete_user
    def test_delete_user_by_wrong_name(self, add_one_user):
        """deleted user by wrong name"""
        name = 'test'
        with allure.step(f"Удаляяем пользователя username={name}"):
            rez = add_one_user.delete_user(name)
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 404"):
            assert rez[0] == 404, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Updated user /user/{username}")
    @allure.story('Обновляем пользователя с некорректным username')
    @pytest.mark.update_user
    def test_update_by_wrong_name(self, add_one_user, params):
        """updated user by wrong name"""
        name = 'test_user'
        z_id = 100
        email = 'test@test.ru'
        with allure.step(f"Обновляем пользователя username={name}, id={z_id}, email={email}"):
            rez = add_one_user.update_user(name, params(id=z_id, email=email))
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 404"):
            assert rez[0] == 404, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Login user into the system  /user/login")
    @allure.story('Выполняем вход пользователя с некорректным username')
    @pytest.mark.login_user
    def test_login_user_by_wrong_name(self, add_one_user):
        """logged user by wrong name and correct password"""
        name = 'test1'
        password = '12345'
        with allure.step(f"Выполняем вход пользователя username={name}, password={password}"):
            rez = add_one_user.login_user(name=name, password=password)
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 400"):
            assert rez[0] == 400, f'Неверный код ответа, получен {rez[0]}'

    @allure.feature("Login user into the system  /user/login")
    @allure.story('Выполняем вход пользователя с некорректным password')
    @pytest.mark.login_user
    def test_login_user_by_wrong_password(self, add_one_user):
        """logged user by correct name and wrong password"""
        name = 'test'
        password = '1'
        with allure.step(f"Выполняем вход пользователя username={name}, password={password}"):
            rez = add_one_user.login_user(name=name, password=password)
        with allure.step(f"Запрос отправлен, проверяем код ответа {rez[0]} == 400"):
            assert rez[0] == 400, f'Неверный код ответа, получен {rez[0]}'
