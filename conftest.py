import pytest
from datetime import datetime
from dm_api_account.account_api import GraphQLAccountApi
from collections import namedtuple



@pytest.fixture
def prepare_user():
    now = datetime.now()
    data = now.strftime("%Y_%m_%d_%H_%M_%S")
    login = f'login_{data}'
    email = f'login_{data}@mail.ru'
    password = '12345678'
    user = namedtuple('User', 'login, email, password')
    return user(login=login, email=email, password=password)


@pytest.fixture
def graphql_account_api():
    client = GraphQLAccountApi(service_name='http://5.63.153.31:5051/')
    return client
