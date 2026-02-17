from datetime import datetime as dt
#Compares the time. If the time is in between 8AM and 4PM, then it prints working hours otherwise it prints fun hours
# 2025-08-28 8 < 16   2025-08-28 
# if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt(dt.now().year,dt.now().month,dt.now().day,18):
#  print("Working hours....")
# else:
#  print("fun hours")
 
 
# print(dt(2025,8,28,10) < dt(2025,8,28,18))
if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 12):
    print("Working hours....")
else:
    print("fun hours")
