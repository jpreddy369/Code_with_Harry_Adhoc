import datetime
from datetime import *
now = datetime.now()
print('now command is bieng printed:', now)
print('date is being printed:', date)

print(f'Date now: {now.day}/{now.month}/{now.year}')
print(f'Time now: {now.hour}:{now.minute}:{now.second}')

#############
tdm = datetime.today()  # today() of datetime class gives date and time
print(tdm)

td = date.today()  # today() of date class gives the date only
print(td)


