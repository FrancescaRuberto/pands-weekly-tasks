# This program outpuys whether or not today is a weekday
# Auhor: Francesca Ruberto

# First, I need to understand how to determine the current day.
# It seems I need to import the datetime module as the first step.

import datetime

# Now that I've imported datetime, I have to specify the current date.
# This allows the program to determine the current day of the week.
today = datetime.date.today()

# Next, I need to categorize the days of the week
# So that the program can distinguish between weekdays and weekend days.
# Since we count from 0, Monday should be 0 and Sunday should be 6.

day_week = today.weekday()

# Finally, I need the program to check which day today is
# and print the appropriate message.
if day_week < 5:
    print("Yes, unfortunately today is weekday")
else:
    print("It is the weekend, yay!")