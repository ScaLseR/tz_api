"""connector for api"""
from json import loads
from dataclasses import dataclass, asdict
from requests import request
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

_METHOD = {_CREATE_USER: 'post', _LOGIN_USER: 'get', _LOGOUT_USER: 'get',
           _DELETE_USER: 'delete', _UPDATED_USER: 'put', _GET_USER_NAME: 'get',
           _CREATE_USER_WITH_LIST: 'post'}


class ApiConnector:
    """class to work with api"""

    def __init__(self, url):
        self.url = url
        self.list_param = []

    def create_user(self, params: ParamsReq = '') -> tuple:
        """create user by params"""
        if params == '':
            response = request(method=_METHOD[_CREATE_USER],
                               url=self.url + _CREATE_USER, timeout=5)
        else:
            response = request(method=_METHOD[_CREATE_USER],
                               url=self.url + _CREATE_USER,
                               json=params.to_dict(), timeout=5)
        with allure.step(f'{_METHOD[_CREATE_USER]} request to: '
                         f'{self.url + _CREATE_USER}'):
            self.logging_request(_METHOD[_CREATE_USER],
                                 self.url + _CREATE_USER, response.text)
            return response.status_code, loads(response.content.decode('utf-8'))

    def create_user_with_list(self, params: ParamsReq = '') -> tuple:
        """create user with list"""
        if params == '':
            response = request(method=_METHOD[_CREATE_USER_WITH_LIST],
                               url=self.url + _CREATE_USER_WITH_LIST, timeout=5)
        else:
            self.list_param.append(params.to_dict())
            response = request(method=_METHOD[_CREATE_USER_WITH_LIST],
                               url=self.url + _CREATE_USER_WITH_LIST,
                               json=self.list_param, timeout=5)
        with allure.step(f'{_METHOD[_CREATE_USER_WITH_LIST]} request to: '
                         f'{self.url + _CREATE_USER_WITH_LIST}'):
            self.logging_request(_METHOD[_CREATE_USER_WITH_LIST],
                                 self.url + _CREATE_USER_WITH_LIST, response.text)
            return response.status_code, loads(response.content.decode('utf-8'))

    def get_user_name(self, name: str = '') -> tuple:
        """get user by name"""
        if name == '':
            response = request(method=_METHOD[_GET_USER_NAME],
                               url=self.url + _GET_USER_NAME, timeout=5)
            with allure.step(f'{_METHOD[_GET_USER_NAME]} request to: '
                             f'{self.url + _GET_USER_NAME}'):
                self.logging_request(_METHOD[_GET_USER_NAME],
                                     self.url + _GET_USER_NAME, response.text)
                return response.status_code,
        else:
            response = request(method=_METHOD[_GET_USER_NAME],
                               url=self.url + _GET_USER_NAME + name, timeout=5)
            with allure.step(f'{_METHOD[_GET_USER_NAME]} request to: '
                             f'{self.url + _GET_USER_NAME + name}'):
                self.logging_request(_METHOD[_GET_USER_NAME],
                                     self.url + _GET_USER_NAME + name, response.text)
                return response.status_code, loads(response.content.decode('utf-8'))

    def delete_user(self, name: str = '') -> tuple:
        """deleted user by name"""
        if name == '':
            response = request(method=_METHOD[_DELETE_USER],
                               url=self.url + _DELETE_USER, timeout=5)
        else:
            response = request(method=_METHOD[_DELETE_USER],
                               url=self.url + _DELETE_USER + name, timeout=5)
            if response.status_code == 200:
                with allure.step(f'{_METHOD[_DELETE_USER]} request to: '
                                 f'{self.url + _DELETE_USER + name}'):
                    self.logging_request(_METHOD[_DELETE_USER],
                                         self.url + _DELETE_USER + name, response.text)
                    return response.status_code, loads(response.content.decode('utf-8'))
        with allure.step(f'{_METHOD[_DELETE_USER]} request to: {self.url + _DELETE_USER}'):
            self.logging_request(_METHOD[_DELETE_USER],
                                 self.url + _DELETE_USER, response.text)
            return response.status_code,

    def update_user(self, name: str = '', params: ParamsReq = '') -> tuple:
        """updated user by name"""
        if name == '':
            response = request(method=_METHOD[_UPDATED_USER],
                               url=self.url + _UPDATED_USER, timeout=5)
        else:
            response = request(method=_METHOD[_UPDATED_USER],
                               url=self.url + _UPDATED_USER + name,
                               json=params.to_dict(), timeout=5)
            with allure.step(f'{_METHOD[_UPDATED_USER]} request to: '
                             f'{self.url + _UPDATED_USER + name}'):
                self.logging_request(_METHOD[_UPDATED_USER],
                                     self.url + _UPDATED_USER + name, response.text)
                return response.status_code, loads(response.content.decode('utf-8'))
        with allure.step(f'{_METHOD[_UPDATED_USER]} request to: '
                         f'{self.url + _UPDATED_USER}'):
            self.logging_request(_METHOD[_UPDATED_USER],
                                 self.url + _UPDATED_USER, response.text)
            return response.status_code,

    def login_user(self, name: str = '', password: str = '') -> tuple:
        """logged user by username and password"""
        response = request(method=_METHOD[_LOGIN_USER], url=self.url + _LOGIN_USER,
                           params=dict(username=name, password=password), timeout=5)
        with allure.step(f'{_METHOD[_LOGIN_USER]} request to: {self.url + _LOGIN_USER}'):
            self.logging_request(_METHOD[_LOGIN_USER],
                                 self.url + _LOGIN_USER, response.text)
            return response.status_code, loads(response.content.decode('utf-8'))

    def logout_user(self) -> tuple:
        """logout user from service"""
        response = request(method=_METHOD[_LOGOUT_USER],
                           url=self.url + _LOGOUT_USER, timeout=5)
        with allure.step(f'{_METHOD[_LOGOUT_USER]} request to: {self.url + _LOGOUT_USER}'):
            self.logging_request(_METHOD[_LOGOUT_USER],
                                 self.url + _LOGOUT_USER, response.text)
            return response.status_code, loads(response.content.decode('utf-8'))

    @staticmethod
    def logging_request(method: str, url: str, text: str):
        """login response and request"""
        logger.info(f'{method} request to: {url}')
        logger.info(f'response text - {text}')
