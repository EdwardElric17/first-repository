import datetime
from time import strftime
date = list((str(input()).split()))
year = int(date[0])
month = int(date[1])
day = int(date[2])
date = datetime.date(year, month, day)
Days = datetime.timedelta(days = int(input()))
delta = date + Days
print(Days)