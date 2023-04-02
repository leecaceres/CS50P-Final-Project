from curses.ascii import isdigit
# from pip._vendor import requests
import re

def main():
    month, day = get_DOB()
    print(get_sign(month, day))
    # get_horoscope(get_sign(month, day))

def get_DOB():

    s = input("What is your birthday? ").strip()

    # mm/dd/yy or mm/dd/yyyy
    if matches := re.search(r"^(\d{1,2})/(\d{1,2})(/\d{2}|\d{4})?$", s):
        month = int(matches.group(1))
        day = int(matches.group(2))

        return check_DOB(month, day)
            
    # month dd, yyyy
    if matches := re.search(r"^(\w+) (\d{1,2})(,? \d{4})?$", s, re.IGNORECASE):
        month = matches.group(1).title()
        day = int(matches.group(2))

        return check_DOB(month, day)

    # dd month, yyyy
    if matches := re.search(r"^(\d{1,2}) (\w+)(,? \d{4})?$", s, re.IGNORECASE):
        month = matches.group(2).title()
        day = int(matches.group(1))

        return check_DOB(month, day)

def check_DOB(month, day):
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


def get_sign(month, day):

    # Sun Signs and corresponding date ranges
    signs = [
        {"name": "Aries", "range": [{"month": "March", "dates": range(21, 32)},
                                    {"month": "April", "dates": range(1, 20)},]},
        {"name": "Taurus", "range": [{"month": "April", "dates": range(20, 31)},
                                    {"month": "May", "dates": range(1, 21)},]},
        {"name": "Gemini", "range": [{"month": "May", "dates": range(21, 32)},
                                    {"month": "June", "dates": range(1, 21)},]},
        {"name": "Cancer", "range": [{"month": "June", "dates": range(21, 31)},
                                    {"month": "July", "dates": range(1, 23)},]},
        {"name": "Leo", "range": [{"month": "July", "dates": range(23, 32)},
                                    {"month": "August", "dates": range(1, 23)},]},
        {"name": "Virgo", "range": [{"month": "August", "dates": range(23, 32)},
                                    {"month": "September", "dates": range(1, 23)},]},
        {"name": "Libra", "range": [{"month": "September", "dates": range(23, 31)},
                                    {"month": "October", "dates": range(1, 23)},]},
        {"name": "Scorpio", "range": [{"month": "October", "dates": range(23, 32)},
                                    {"month": "November", "dates": range(1, 22)},]},
        {"name": "Sagittarius", "range": [{"month": "November", "dates": range(23, 32)},
                                    {"month": "December", "dates": range(1, 22)},]},
        {"name": "Capricorn", "range": [{"month": "December", "dates": range(22, 32)},
                                    {"month": "January", "dates": range(1, 20)},]},
        {"name": "Aquarius", "range": [{"month": "January", "dates": range(20, 30)},
                                    {"month": "February", "dates": range(1, 19)},]},
        {"name": "Pisces", "range": [{"month": "February", "dates": range(19, 32)},
                                    {"month": "March", "dates": range(1, 21)},]},
    ]

    for sign in signs:
        for m in sign["range"]:
            if m["month"] == month:
                if day in m["dates"]:
                    return sign["name"]

    raise ValueError("DOB/Sign not matched")

def get_horoscope(sign):
    ...

if __name__ == "__main__":
    main()