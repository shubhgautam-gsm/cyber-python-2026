from datetime import datetime, timedelta

# Example: video uploaded on 28th August 2025
upload_date = datetime(2025, 8, 26)


# Today
current_date = datetime.today() #(2025,9,2)   2025-2025,9-8(30),(30+2)-26=6 
 
# Difference in days
period_complete = (current_date - upload_date).days

if period_complete <= 7:
    print('video uploaded within week')
elif period_complete <= 30:
    print('video uploaded within month')
elif period_complete <= 365:
    print('video uploaded within year')
else:
    print('video is older than a year')
