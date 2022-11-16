import re

months = {
    '01': 31,
    '02': 28,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31
}

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return False
        if year % 400 == 1:
            return True
        return True
    return False

def isDateValid(date):
    date_re = re.compile(r'(\d\d)/(\d\d)/(\d{4})')
    date_search = date_re.search(date)
    day = date_search.group(1)
    month = date_search.group(2)
    year = date_search.group(3)
    day = int(day)
    year = int(year)
    if isLeapYear(year):
        if month == '02':
            if day > 29:
                print('Leap year February date invalid')
                return False
            return True
    if day > months[month]:
        print('Day exceeds month')
        return False
    if int(month) > 12:
        print('Month exceeds 12')
        return False
    return True
            
testDate = [
    '30/01/2020', # Valid
    '14/11/2022', # Valid
    '31/01/2022', # Valid
    '28/02/2020', # Valid
    '29/02/2020', # Valid
    '29/02/2021', # Invalid
    '31/04/2021'] # Invalid

for date in testDate:
    if isDateValid(date):
        print(date + ' is VALID')
    else: print(date + ' is INVALID')
    print('')
