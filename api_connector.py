"""connector for api"""
from json import dumps, loads
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

    def to_json(self):
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

    def create_user(self, params: ParamsReq):
        """create user"""
        response = requests.post(url=self.url + _CREATE_USER, json=params.to_json())
        if response.status_code == 200:
            return response.status_code, loads(response.content.decode('utf-8'))
        return response.status_code

