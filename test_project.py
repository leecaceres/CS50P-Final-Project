import pytest
from project import get_DOB, check_DOB, get_endpoint_type, get_sign, get_day, print_sign,get_daily_horoscope, get_weekly_horoscope, get_monthly_horoscope

def test_get_DOB():
    assert get_DOB("05/13/2003") == ("May", 13)
    assert get_DOB("Nov 05, 2003") == ("November", 5)
    assert get_DOB("01 August 2003") == ("August", 1)
    

def test_check_DOB():
    assert check_DOB(5, 13) == ("May", 13)
    assert check_DOB("Apr", 20) == ("April", 20)
    assert check_DOB("July", 11) == ("July", 11)

    # Catch invalid days
    with pytest.raises(ValueError):
        check_DOB(1, 0)
    with pytest.raises(ValueError):
        check_DOB(1, 32)
    with pytest.raises(ValueError):
        check_DOB(2, 30)

    # Catch invalid months
    with pytest.raises(ValueError):
        check_DOB(0, 1)
    with pytest.raises(ValueError):
        check_DOB(13, 1)
    

def test_get_endpoint_type():
    ...    


def test_get_sign():
    assert get_sign("May", 13) == "Taurus"
    assert get_sign("August", 13) == "Leo"
    assert get_sign("November", 13) == "Scorpio"


def test_get_day():
    ...


def test_print_sign():
    ...

    
def test_get_daily_horoscope():
    ...


def test_get_weekly_horoscope():
    ...


def test_get_monthly_horoscope():
    ...