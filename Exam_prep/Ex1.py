import datetime

date=None

while date is None:
    try:
        year = int(input("Enter year:"))
        month = int(input("Enter month:"))
        day = int(input("Enter day:"))

        date = datetime.date(year, month, day)
    except:
        print("The date is not correct!")

print(date+datetime.timedelta(days=1))