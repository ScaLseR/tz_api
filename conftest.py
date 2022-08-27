"""fixtures"""
import pytest
from api_connector import ApiConnector, ParamsReq
import logging

logger = logging.getLogger("test_api")


@pytest.fixture(scope='function', autouse=True)
def logging():
    """write to log start and stop test"""
    logger.info('Start test')
    yield
    logger.info('Stop test')


@pytest.fixture(scope='function')
def api_con(url):
    """connection to api"""
    api_con = ApiConnector(url)
    return api_con


@pytest.fixture(scope='function')
def params():
    """created data class for parameters to requests"""
    params = ParamsReq
    return params


@pytest.fixture(scope='function')
def url():
    """get api url """
    url = 'https://petstore.swagger.io/v2'
    return url


@pytest.fixture(scope='function')
def add_one_user(api_con, params):
    """added one user by name"""
    _ = api_con.create_user(params(id=100, username='test', password='12345'))
    yield api_con
    _ = api_con.delete_user('test')
