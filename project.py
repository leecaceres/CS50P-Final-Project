import re

def main():
    month, day = get_DOB()
    print(get_sign(month, day))

def get_DOB():
    
    months = [
        {"month": "January", "number": 1, "length": 31},
        {"month": "February", "number": 2, "length": 29},
        {"month": "March", "number": 3, "length": 31},
        {"month": "April", "number": 4, "length": 30},
        {"month": "May", "number": 5, "length": 31},
        {"month": "June", "number": 6, "length": 30},
        {"month": "July", "number": 7, "length": 31},
        {"month": "August", "number": 8, "length": 31},
        {"month": "September", "number": 9, "length": 30},
        {"month": "October", "number": 10, "length": 31},
        {"month": "November", "number": 11, "length": 30},
        {"month": "December", "number": 12, "length": 31},
    ]

    s = input("What is your birthday? ").strip()

    # mm/dd/yy or mm/dd/yyyy
    if matches := re.search(r"^(\d{2})/(\d{2})/(\d{2}|\d{4})$", s):
        month = int(matches.group(1))
        day = int(matches.group(2))

        # Check if day is valid
        if day <= 0 or day > 31:
                raise ValueError("Invalid date")
        
        for m in months:         
            # Check if date in month length
            if m["number"] == month:
                if day > m["length"]:
                    raise ValueError
                month = m["month"]
                return(month, day)
            
        raise ValueError("Invalid date")
            
    # month dd, yyyy
    if matches := re.search(r"(.+) (\d{1,2}),? (\d{4})", s, re.IGNORECASE):
        if months[matches.group(1)] in months:
            print()


    # dd month, yyyy
    # if matches := re.search(r"(\d{1,2}) (.+),? (\d{4})", s, re.IGNORECASE):
        # ...

def get_sign(month, day):
    return "taurus"

# def get_horoscope():
#     ...

if __name__ == "__main__":
    main()