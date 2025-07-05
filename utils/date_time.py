from datetime import datetime, date
import jdatetime
import pytz


def date_to_shamsi(date_input):
    if isinstance(date_input, date):
        date_utc = datetime.combine(date_input, datetime.min.time()).replace(tzinfo=pytz.utc)
    else:
        raise ValueError("Input must be a date (datetime.date) object.")

    tehran_tz = pytz.timezone('Asia/Tehran')
    date_tehran = date_utc.astimezone(tehran_tz)
    
    return jdatetime.datetime.fromgregorian(
        year=date_tehran.year,
        month=date_tehran.month,
        day=date_tehran.day
    ).strftime('%Y/%m/%d')
