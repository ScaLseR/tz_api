"""connector for api"""
from json import loads
from dataclasses import dataclass, asdict
import requests
import allure
import logging

logger = logging.getLogger("test_api")


@dataclass
class ParamsReq:
    """structure for requests parameters"""
    id: int = 0
    username: str = ''
    firstName: str = ''
    lastName: str = ''
    email: str = ''
    password: str = ''
    phone: str = ''
    userStatus: int = 0

    def to_dict(self):
        """convert to dict structure ParamsReq"""
        return asdict(self)


_CREATE_USER = '/user'
_LOGIN_USER = '/user/login'
_LOGOUT_USER = '/user/logout'
_DELETE_USER = '/user/'
_UPDATED_USER = '/user/'
_GET_USER_NAME = '/user/'
_CREATE_USER_WITH_LIST = '/user/createWithList'


class ApiConnector:
    """class to work with api"""

    def __init__(self, url):
        self.url = url
        self.list_param = []

    def create_user(self, params: ParamsReq = '') -> tuple:
        """create user by params"""
        if params == '':
            response = requests.post(url=self.url + _CREATE_USER, timeout=5)
        else:
            response = requests.post(url=self.url + _CREATE_USER,
                                     json=params.to_dict(), timeout=5)
        with allure.step(f'POST request to: {self.url + _CREATE_USER}'):
            logger.info(response.text)
            return response.status_code, loads(response.content.decode('utf-8'))

    def create_user_with_list(self, params: ParamsReq = '') -> tuple:
        """create user with list"""
        if params == '':
            response = requests.post(url=self.url + _CREATE_USER_WITH_LIST, timeout=5)
        else:
            self.list_param.append(params.to_dict())
            response = requests.post(url=self.url + _CREATE_USER_WITH_LIST,
                                     json=self.list_param, timeout=5)
        with allure.step(f'POST request to: {self.url + _CREATE_USER_WITH_LIST}'):
            logger.info(response.text)
            return response.status_code, loads(response.content.decode('utf-8'))

    def get_user_name(self, name: str = '') -> tuple:
        """get user by name"""
        if name == '':
            response = requests.get(url=self.url + _GET_USER_NAME, timeout=5)
            with allure.step(f'GET request to: {self.url + _GET_USER_NAME}'):
                logger.info(response.text)
                return response.status_code,
        else:
            response = requests.get(url=self.url + _GET_USER_NAME + name, timeout=5)
            with allure.step(f'GET request to: {self.url + _GET_USER_NAME + name}'):
                logger.info(response.text)
                return response.status_code, loads(response.content.decode('utf-8'))

    def delete_user(self, name: str = '') -> tuple:
        """deleted user by name"""
        if name == '':
            response = requests.delete(url=self.url + _DELETE_USER, timeout=5)
        else:
            response = requests.delete(url=self.url + _DELETE_USER + name, timeout=5)
            if response.status_code == 200:
                with allure.step(f'DELETE request to: {self.url + _DELETE_USER + name}'):
                    logger.info(response.text)
                    return response.status_code, loads(response.content.decode('utf-8'))
        with allure.step(f'DELETE request to: {self.url + _DELETE_USER}'):
            logger.info(response.text)
            return response.status_code,

    def update_user(self, name: str = '', params: ParamsReq = '') -> tuple:
        """updated user by name"""
        if name == '':
            response = requests.put(url=self.url + _UPDATED_USER, timeout=5)
        else:
            response = requests.put(url=self.url + _UPDATED_USER + name,
                                    json=params.to_dict(), timeout=5)
            with allure.step(f'DELETE request to: {self.url + _UPDATED_USER + name}'):
                logger.info(response.text)
                return response.status_code, loads(response.content.decode('utf-8'))
        with allure.step(f'PUT request to: {self.url + _UPDATED_USER}'):
            logger.info(response.text)
            return response.status_code,

    def login_user(self, name: str = '', password: str = '') -> tuple:
        """logged user by username and password"""
        response = requests.get(url=self.url + _LOGIN_USER,
                                params=dict(username=name, password=password), timeout=5)
        with allure.step(f'GET request to: {self.url + _LOGIN_USER}'):
            logger.info(response.text)
            return response.status_code, loads(response.content.decode('utf-8'))

    def logout_user(self) -> tuple:
        """logout user from service"""
        response = requests.get(url=self.url + _LOGOUT_USER, timeout=5)
        with allure.step(f'GET request to: {self.url + _LOGOUT_USER}'):
            logger.info(response.text)
            return response.status_code, loads(response.content.decode('utf-8'))
