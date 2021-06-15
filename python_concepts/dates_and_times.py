import datetime

today = datetime.date(2021, 6, 14)
# print(today)

now = datetime.datetime.now()
# print(now)

tomorrow = now + datetime.timedelta(days=1, hours=6)
new_years_day = datetime.datetime(2022, 1, 1, second=1)
print(new_years_day)

print()
