import calendar

def Generator_Months():
    for i in range(13):
        yield calendar.month_name[i]


for i in Generator_Months():
    print(i, end=' ')