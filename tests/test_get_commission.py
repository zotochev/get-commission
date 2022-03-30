import pytest

from get_commission import get_commission


@pytest.mark.parametrize("date, expected_result",
                         [("2010-01-01", 0.1),
                          ("2010-02-01", 0.1),
                          ("2010-03-01", 0.1),
                          ("2010-04-01", 0.1),
                          ("2010-05-01", 0.1),
                          ("2010-06-01", 0.15),
                          ("2010-07-01", 0.15),
                          ("2010-08-01", 0.15),
                          ("2010-09-01", 0.15),
                          ("2010-10-01", 0.1),
                          ("2010-11-01", 0.1),
                          ("2010-12-01", 0.1),
                          ("2010-12-01 ", 0.1),
                          (" 2010-12-01", 0.1),
                          (" 2010-12-01 ", 0.1),
                          ("      2010-12-01", 0.1),
                          ("2010-12-01           ", 0.1),
                          ("       2010-12-01         ", 0.1),
                          ])
def test_correct(date: str, expected_result: float):
    assert get_commission(date) == expected_result


def test_empty_string():
    with pytest.raises(ValueError):
        get_commission('')


def test_not_date_string():
    with pytest.raises(ValueError):
        get_commission('Hello!')


def test_wrong_format_0():
    with pytest.raises(ValueError):
        get_commission('01-01-2010')


def test_wrong_format_1():
    with pytest.raises(ValueError):
        get_commission('2009 - 02 - 19')


def test_wrong_format_2():
    with pytest.raises(ValueError):
        get_commission('2009 02 19')


def test_impossible_date_0():
    with pytest.raises(ValueError):
        get_commission('01-13-2010')


def test_impossible_date_1():
    with pytest.raises(ValueError):
        get_commission('40-11-2010')


def test_impossible_date_2():
    with pytest.raises(ValueError):
        get_commission('29-02-2019')


def test_wrong_type_int():
    with pytest.raises(AttributeError):
        get_commission(1)


def test_wrong_type_bool():
    with pytest.raises(AttributeError):
        get_commission(True)


def test_wrong_type_none():
    with pytest.raises(AttributeError):
        get_commission(None)
