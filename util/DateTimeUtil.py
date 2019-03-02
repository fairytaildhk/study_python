import datetime


def getTodayDateTime():
    return datetime.date.today()


def getFutureDateTime(days):
    return datetime.date.today() + datetime.timedelta(days=days)


def get_future_datetime_format(days, tmp_format="%Y-%m-%d %H:%M:%S"):
    return (datetime.datetime.now() + datetime.timedelta(days=days)).strftime(tmp_format)
