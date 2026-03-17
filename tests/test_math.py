import pytest


def add_sum(a, b):
    return a + b


@pytest.mark.parametrize("param_set", [(2, 3), (3, 4), (5, 7)], indirect=True)
def test_add(param_set):
    assert (
        add_sum(param_set[0], param_set[1]) == param_set[2]
    ), "сумма не равна ожидаемой"


@pytest.mark.type
def test_type_result():
    assert isinstance(add_sum(2, 3), int), \
        "не соответствует ожидаемому типу данных"
