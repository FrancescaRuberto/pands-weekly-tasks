# This program outpuys whether or not today is a weekday
# Auhor: Francesca Ruberto

#First thing, I need to understand how to work out what day it is. 
# Apparently I need to import datetime as first step

import datetime

# Once imported datetime I should specify the current date
# In this way the program at the end should understand which day it is
today = datetime.date.today()

# Now I need to "categorize" the days of week
# So the program can distinguish between weekdays and weekend days
# Since we count from 0, Monday should be 0 and Sunday 6

day_week = today.weekday()

# Now I need the program to check which day is today
if day_week < 5:
    print("Yes, unfortunately today is weekday")
else:
    print("It is the weekend, yay!")