# the datetime Module

from datetime import datetime

date = datetime.strptime("July 16, 2022", 
                         "%B %d, %Y")
weekday_name = date.strftime("%A")
print(weekday_name)

from datetime import datetime as dt

date = dt.strptime("August 22, 2024",
                   "%B %d, %Y")
weekday_name = date.strftime("%A")
print(weekday_name)