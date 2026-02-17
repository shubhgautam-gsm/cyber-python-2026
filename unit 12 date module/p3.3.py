import time

# get current day as integer
upload_day = 28 #28  
current_day=int(time.strftime('%d')) #2
period_complete=current_day-upload_day
# print(current_day)
# diff=2-28 =-26
if period_complete <= 7:
    print('video uploaded within week')
elif period_complete<=30:
    print('video upload  within month')
elif period_complete<=365:
    print('video upload with year')

# x=8+1 
# register=8
# diff=x-register