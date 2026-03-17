import pytest


@pytest.fixture(params=('BTC', 'ETH'), scope='session')
def get_data(request):
    token = request.param
    response_data = [[]]
    match token:
        case 'BTC':
            from utils.btc_response import BTC_RESPONSE as response_data
        case 'ETH':
            from utils.eth_response import ETH_RESPONSE as response_data
        case _:
            raise ValueError("Wrong crypto's name")
    
    return token, response_data['result']['items']

""" @pytest.fixture(params=('tokenId', 'currencyId', 
                        'count_offers', 'valid_price', 'valid_quantity'),
                scope='session')
def get_marker(request):
    return request.param """