import pytest
from random import randint


pytest_plugins = [
    'fixtures.fixtures_offers_data',
]

@pytest.fixture
def param_set(request):
    a, b = request.param
    a_r = randint(0, a)
    b_r = randint(0, b)
    result = randint(0, a + b)
    return (a_r, b_r, result)