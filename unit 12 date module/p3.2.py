import time

# get current month as integer
current_month = int(time.strftime("%m"))

# example: suppose user paid in current month
period = current_month + 1      # next renewal month
period_complete = current_month - period

if period_complete <= 7:
    print('renew payment to get premium access')
else:
    print('you have access to premium')


# x=8+1 
# register=8
# diff=x-register