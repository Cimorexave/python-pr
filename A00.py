import math
from datetime import datetime as dt

def summing(a_list: list) -> float:
    result: float = 0.0
    for el in a_list:
        try:
            result += float(el)
        except:
            continue
    return result

assert math.isclose(summing([-0.3, 0.3]), 0.0), summing([-0.3, 0.3])
assert math.isclose(summing([2.3, "4.5", "bla"]), 6.8), summing([2.3, "4.5", "bla"])
assert math.isclose(summing([]), 0.0), summing([])

def mins_since(a_date: str) -> int:
    format_code = "%d.%m.%Y %H:%M:%S"
    REF_DATE = dt.strptime("01.10.2025 00:00:00", format_code)
    try:
        parsed_date_object = dt.strptime(a_date, format_code)
        print(f'date object: {parsed_date_object}')
    except ValueError as e:
        print(f'invalid string input date format: {e}')
        raise ValueError()
    if parsed_date_object >= REF_DATE:
        print(f'inputed date is after the reference date.')
        return -1
    
    dif = REF_DATE - parsed_date_object
    return int(dif.total_seconds() / 60)

assert mins_since("30.09.2025 23:00:00") == 60 , mins_since("30.09.2025 23:00:00")
assert mins_since("01.10.2025 12:00:00") == -1, mins_since("01.10.2025 12:00:00") 
assert mins_since("30.09.2025 23:58:00") == 2, mins_since("30.09.2025 23:58:00")
assert mins_since("30.09.2025 23:59:00") == 1, mins_since("30.09.2025 23:59:00")
assert mins_since("29.09.2025 00:00:00") == 2880, mins_since("29.09.2025 00:00:00") 