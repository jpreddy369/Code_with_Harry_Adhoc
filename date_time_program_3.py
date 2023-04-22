from datetime import *
##################
#Combine date and time by using combine() method of datetime class
d = date(2012, 1, 11)  # d =date(2012,01,11)  # 01 format will give you error
t = time(15, 30)
dt = datetime.combine(d,t)
print(dt)

##########################
#datetime class can be created in 3 ways: 1. datetime.now()  2. datetime.combine(d, t)  3. datetime(2016, 6, 24, 18, 30)
dt1 = datetime.now()
print(dt1)

dt2 = datetime.combine(d, t)
print(dt2)

dt3 = datetime(2023, 1, 11, 10, 9)
print(dt3)

# change the content by replace()


