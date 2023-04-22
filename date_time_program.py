import time
epoch = time.time()
print(epoch)  # 1673408501.1801777
df = time.localtime(epoch) # time.struct_time(tm_year=2023, tm_mon=1, tm_mday=11, tm_hour=9, tm_min=12, tm_sec=44, tm_wday=2, tm_yday=11, tm_isdst=0)
print(df)
print('current date is: ',df.tm_year,'-',df.tm_mon,'-',df.tm_mday)
y = df.tm_year
m = df.tm_mon
d = df.tm_mday
print(f'current date is {y}-{m}-{d}')

t = time.ctime(epoch)
print(t)