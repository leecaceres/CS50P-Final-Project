from pip._vendor import requests
import re
import pyfiglet
import json

def main():
    # Get user's Date of Birth (DOB)
    s = input("What is your birthday? ").strip()
    month, day = get_DOB(s)

    # Get user's sign and symbol
    sign, symbol = get_sign(month, day)

    # Get endpoint type: daily, weekly, monthly
    print("--------------------------------------------")
    x = input("Which horoscope would you like to see: \n[1] Daily \n[2] Weekly \n[3] Monthly\nEnter: ").strip()
    print("--------------------------------------------")
    option = get_endpoint_type(x)

    # Based on option, get horoscope
    if option == 1:
        d = input("Which daily horoscope would you like to see:\n[1] Today's\n[2] Tomorrow's\n[3] Yesterday's\nEnter: ").strip()
        print("--------------------------------------------")
        print()
        day = get_day(d)
        print(print_sign(sign))
        get_daily_horoscope(sign, symbol, day)

    elif option == 2:
        print()
        print(print_sign(sign))
        get_weekly_horoscope(sign, symbol)

    elif option == 3:
        print()
        print(print_sign(sign))
        get_weekly_horoscope(sign, symbol)


def get_DOB(s):
    # mm/dd/yy or mm/dd/yyyy
    if matches := re.search(r"^(\d{1,2})/(\d{1,2})(?:/)?(\d{2}|\d{4})?$", s):
        month = int(matches.group(1))
        day = int(matches.group(2))

        return check_DOB(month, day)
            
    # month dd, yyyy
    if matches := re.search(r"^(\w+) (\d{1,2})(?:st|nd|rd|th)?(,? \d{4})?$", s, re.IGNORECASE):
        month = matches.group(1).title()
        day = int(matches.group(2))

        return check_DOB(month, day)

    # dd month, yyyy
    if matches := re.search(r"^(\d{1,2}) (\w+)(,? \d{4})?$", s, re.IGNORECASE):
        month = matches.group(2).title()
        day = int(matches.group(1))

        return check_DOB(month, day)
    
    raise ValueError("Invalid date. Correct format: 'mm/dd/yyyy', 'month dd, yyyy', or 'dd month, yyyy'")


def check_DOB(month, day):
    # List of month dicts
    months = [
        {"month": "January", "number": 1, "length": 31, "short": "Jan"},
        {"month": "February", "number": 2, "length": 29, "short": "Feb"},
        {"month": "March", "number": 3, "length": 31, "short": "Mar"},
        {"month": "April", "number": 4, "length": 30, "short": "Apr"},
        {"month": "May", "number": 5, "length": 31, "short": None},
        {"month": "June", "number": 6, "length": 30, "short": "Jun"},
        {"month": "July", "number": 7, "length": 31, "short": "Jul"},
        {"month": "August", "number": 8, "length": 31, "short": "Aug"},
        {"month": "September", "number": 9, "length": 30, "short": "Sep"},
        {"month": "October", "number": 10, "length": 31, "short": "Oct"},
        {"month": "November", "number": 11, "length": 30, "short": "Nov"},
        {"month": "December", "number": 12, "length": 31, "short": "Dec"},
    ]

    # Check if day is valid
    if day <= 0 or day > 31:
        raise ValueError("Invalid day")
    
    for m in months:
        # If month is int, find name
        if isinstance(month, int):
            if month <=0 or month > 12:
                raise ValueError("Invalid month")
            if m["number"] == month:
                month = m["month"]

        # If shortened month name used, switch to full
        if m["short"] == month:
            month = m["month"]
        
        # Check if month name + date are valid
        if m["month"] == month:
            # Check day in length
            if day > m["length"]:
                raise ValueError("Invalid day")
            
            return(month, day)
                
    raise ValueError("Invalid")


def get_endpoint_type(x):
    # Check input is matches daily, return 1
    if matches:= re.search(r"(1|[1]|Daily)", x, re.IGNORECASE):
        return 1

    # Check input matches weekly, return 2 
    if matches:= re.search(r"(2|[2]|Weekly)", x, re.IGNORECASE):
        return 2

    # Check input matches monthly, return 3
    if matches:= re.search(r"(3|[3]|Monthly)", x, re.IGNORECASE):
        return 3

    # Raise ValueErrors for invalid input
    raise ValueError("Invalid input. Correct format: either '1', '[1]', or 'daily')")


def get_sign(month, day):
    # Sun Signs and corresponding date ranges
    signs = [
        {"name": "Aries", "symbol": "♈︎", "range": [{"month": "March", "dates": range(21, 32)},
                                    {"month": "April", "dates": range(1, 20)},]},
        {"name": "Taurus", "symbol": "♉︎","range": [{"month": "April", "dates": range(20, 31)},
                                    {"month": "May", "dates": range(1, 21)},]},
        {"name": "Gemini", "symbol": "♊︎","range": [{"month": "May", "dates": range(21, 32)},
                                    {"month": "June", "dates": range(1, 21)},]},
        {"name": "Cancer", "symbol": "♋︎","range": [{"month": "June", "dates": range(21, 31)},
                                    {"month": "July", "dates": range(1, 23)},]},
        {"name": "Leo", "symbol": "♌︎","range": [{"month": "July", "dates": range(23, 32)},
                                    {"month": "August", "dates": range(1, 23)},]},
        {"name": "Virgo", "symbol": "♍︎","range": [{"month": "August", "dates": range(23, 32)},
                                    {"month": "September", "dates": range(1, 23)},]},
        {"name": "Libra", "symbol": "♎︎","range": [{"month": "September", "dates": range(23, 31)},
                                    {"month": "October", "dates": range(1, 23)},]},
        {"name": "Scorpio", "symbol": "♏︎","range": [{"month": "October", "dates": range(23, 32)},
                                    {"month": "November", "dates": range(1, 22)},]},
        {"name": "Sagittarius", "symbol": "♐︎","range": [{"month": "November", "dates": range(23, 32)},
                                    {"month": "December", "dates": range(1, 22)},]},
        {"name": "Capricorn", "symbol": "♑︎","range": [{"month": "December", "dates": range(22, 32)},
                                    {"month": "January", "dates": range(1, 20)},]},
        {"name": "Aquarius", "symbol": "♒︎","range": [{"month": "January", "dates": range(20, 30)},
                                    {"month": "February", "dates": range(1, 19)},]},
        {"name": "Pisces", "symbol": "♓︎","range": [{"month": "February", "dates": range(19, 32)},
                                    {"month": "March", "dates": range(1, 21)},]},
    ]

    # Return sign and name
    for sign in signs:
        for m in sign["range"]:
            if m["month"] == month:
                if day in m["dates"]:
                    return (sign["name"], sign["symbol"])

    raise ValueError("DOB/Sign not matched")


def get_day(day):
    # Check input is matches today, return "today"
    if matches:= re.search(r"(1|[1]|Today('s)?)", day, re.IGNORECASE):
        return "today"

    # Check input matches tomorrow, return "tomorrow"
    if matches:= re.search(r"(2|[2]|Tomorrow('s)?)", day, re.IGNORECASE):
        return "tomorrow"
    
    # Check input matches yesterday, return "yesterday"
    if matches:= re.search(r"(3|[3]|Yesterday('s)?)", day, re.IGNORECASE):
        return "yesterday"

    # Raise ValueErrors for invalid input
    raise ValueError("Invalid input. Correct format: either '1', '[1]', or 'Today')")


def print_sign(sign):
    # Print astrological sign using ascii art
    result = pyfiglet.figlet_format(f"{sign}!")
    return result


def get_daily_horoscope(sign, symbol, day):
    # URL and PARAMS – uncomment line below and insert IP Address
    # URL = f"http://[insert local IP Address]/api/v1/get-horoscope/daily"
    PARAMS = {"sign": sign, "day": day}

    # GET request daily horoscope
    response = requests.get(url = URL, params=PARAMS)
    data = response.json()

    # Print date
    data = data["data"].split("- ")
    print(f"{data[0]} {symbol}", end=":\n")
    print()

    # Print horoscope, 10 words per line
    txt = re.split(" ", data[1])
    for i in range(0, len(txt), 10):
        print(*txt[i:i + 10])
    print()
    print("--------------------------------------------")


def get_weekly_horoscope(sign, symbol):
    # URL and PARAMS – uncomment line below and insert IP Address
    # URL = f"http://[insert local IP Address]/api/v1/get-horoscope/weekly"
    PARAMS = {"sign": sign}

    # GET request weekly horoscope
    response = requests.get(url = URL, params=PARAMS)
    data = response.json()

    # Print week range
    data = data["data"].split("- ")
    print(f"{data[0]} {symbol}", end=":\n")
    print()

    # Print horoscope, 15 words per line
    txt = re.split(" ", data[1])
    for i in range(0, len(txt), 15):
        print(*txt[i:i + 15])
    print()
    print("--------------------------------------------")


def get_monthly_horoscope(sign, symbol):
    # URL and PARAMS – uncomment line below and insert IP Address
    # URL = f"http://[insert local IP Address]/api/v1/get-horoscope/monthly"
    PARAMS = {"sign": sign}

    # GET request monthly horoscope
    response = requests.get(url = URL, params=PARAMS)
    data = response.json()

    # Print month
    data = data["data"].split("- ")
    print(f"{data[0]} {symbol}", end=":\n")
    print()

    # Print horoscope, 15 words per line
    txt = re.split(" ", data[1])
    for i in range(0, len(txt), 15):
        print(*txt[i:i + 15])
    print()
    print("--------------------------------------------")


if __name__ == "__main__":
    main()
