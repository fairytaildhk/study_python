import datetime


def record_arrive_time():
    arrive_time = datetime.datetime.today().time()
    print(arrive_time)
    sql = "insert into attendance_sheet(`name`, `arrive_time`) VALUES ('test', '2019-3-02')"



if __name__ == '__main__':
    record_arrive_time()