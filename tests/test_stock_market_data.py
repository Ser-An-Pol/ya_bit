import pytest


@pytest.mark.parametrize(
    "get_marker",
    [
        pytest.param("tokenId", marks=pytest.mark.token),
        pytest.param("currencyId", marks=pytest.mark.currency),
        pytest.param("count_offers", marks=pytest.mark.count_offers),
        pytest.param("valid_price", marks=pytest.mark.valid_price),
        pytest.param("valid_quantity", marks=pytest.mark.valid_price),
    ],
)
def test_offer(get_data, get_marker):
    match get_marker:
        case "tokenId":
            for offer in get_data[1]:
                assert (
                    get_data[0] == offer["tokenId"]
                ), f"Wrong token: {offer['tokenId']} \
                        instead {get_data[0]}"
        case "currencyId":
            for offer in get_data[1]:
                assert (
                    "RUB" == offer["currencyId"]
                ), f"Wrong currency: {offer['currencyId']} instead RUB"
        case "count_offers":
            assert (
                len(get_data[1]) == 10
            ), f"Wrong count of offers: {len(get_data[1])} instead 10"
        case "valid_price":
            for offer in get_data[1]:
                assert float(offer["price"]) > 0, \
                    "Wrong price! It must be positive"
        case "valid_quantity":
            for offer in get_data[1]:
                assert (
                    float(offer["quantity"]) > 0
                ), "Wrong quantity! It must be positive"
