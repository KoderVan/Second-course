import datetime


def add_days(year, month, day, days_number):
    current_date = datetime.date(year, month, day)
    delta = datetime.timedelta(days=days_number)
    new_date = current_date + delta
    cleared_date = new_date.strftime('%Y %#m %#d')
    return cleared_date


def main():
    year, month, day = [int(i) for i in input().split()]
    days = int(input())
    new_date = add_days(year, month, day, days)
    print(new_date)


if __name__ == '__main__':
    main()
