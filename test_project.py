import pytest
import pyfiglet
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
    # Daily
    assert get_endpoint_type("1") == 1
    assert get_endpoint_type("[1]") == 1
    assert get_endpoint_type("Daily") == 1
    # Weekly
    assert get_endpoint_type("2") == 2
    assert get_endpoint_type("[2]") == 2
    assert get_endpoint_type("Weekly") == 2
    # Monthly
    assert get_endpoint_type("3") == 3
    assert get_endpoint_type("[3]") == 3
    assert get_endpoint_type("Monthly") == 3


def test_get_sign():
    assert get_sign("May", 13) == ("Taurus", "♉︎")
    assert get_sign("August", 13) == ("Leo", "♌︎")
    assert get_sign("November", 13) == ("Scorpio", "♏︎")


def test_get_day():
    # Today
    assert get_day("1") == "today"
    assert get_day("[1]") == "today"
    assert get_day("Today") == "today"
    assert get_day("Today's") == "today"
    # Tomorrow
    assert get_day("2") == "tomorrow"
    assert get_day("[2]") == "tomorrow"
    assert get_day("Tomorrow") == "tomorrow"
    assert get_day("Tomorrow's") == "tomorrow"
    # Yesterday
    assert get_day("3") == "yesterday"
    assert get_day("[3]") == "yesterday"
    assert get_day("Yesterday") == "yesterday"
    assert get_day("Yesterday's") == "yesterday"


def test_print_sign():
    result_1 = pyfiglet.figlet_format(f"Taurus!")
    result_2 = print_sign("Taurus")
    assert result_1 == result_2
    
    
def test_get_daily_horoscope(capsys):
    get_daily_horoscope("Taurus", "♉︎", "today")
    captured = capsys.readouterr()
    assert captured.out != None


def test_get_weekly_horoscope(capsys):
    get_weekly_horoscope("Taurus", "♉︎")
    captured = capsys.readouterr()
    assert captured.out != None


def test_get_monthly_horoscope(capsys):
    get_monthly_horoscope("Taurus", "♉︎")
    captured = capsys.readouterr()
    assert captured.out != None