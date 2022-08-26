"""connector for api"""
from json import loads
from dataclasses import dataclass, asdict
import requests


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
            response = requests.post(url=self.url + _CREATE_USER)
        else:
            response = requests.post(url=self.url + _CREATE_USER, json=params.to_dict())
        return response.status_code, loads(response.content.decode('utf-8'))

    def create_user_with_list(self, params: ParamsReq = '') -> tuple:
        """create user with list"""
        if params == '':
            response = requests.post(url=self.url + _CREATE_USER_WITH_LIST)
        else:
            self.list_param.append(params.to_dict())
            response = requests.post(url=self.url + _CREATE_USER_WITH_LIST, json=self.list_param)
        return response.status_code, loads(response.content.decode('utf-8'))

    def get_user_name(self, name: str = '') -> tuple:
        """get user by name"""
        if name == '':
            response = requests.get(url=self.url + _GET_USER_NAME + ' ')
        else:
            response = requests.get(url=self.url + _GET_USER_NAME + name)
        return response.status_code, loads(response.content.decode('utf-8'))
