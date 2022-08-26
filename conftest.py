"""fixtures"""
import pytest
from api_connector import ApiConnector, ParamsReq


@pytest.fixture(scope="function")
def api_con(url):
    """connection to api"""
    api_con = ApiConnector(url)
    return api_con


@pytest.fixture(scope="function")
def params():
    """created data class for parameters to requests"""
    params = ParamsReq
    return params


@pytest.fixture(scope='function')
def url():
    """get api url """
    url = 'https://petstore.swagger.io/v2'
    return url
