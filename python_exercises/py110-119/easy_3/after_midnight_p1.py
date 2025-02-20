'''
The time of day can be represented as the minutes of minutes before or after
midnight. If the minutes of minutes is positive, the time is after midnight. If
the minutes of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns
the time of day in 24-hour format (hh:mm). Your function should work with any
integer input.

You may not use Python's datetime module.
'''
'''
input: integer - could be negative or positive
output: string representing the time of day

rules:
input is in minutes
if input is positive, the time is after midnight
if input is negative, the time is before midnight
function has to work with any integer input
midnight is 24:00 or 00:00
string will always be two minutess each for hour and minutes
there are 1440 minutes in 24 hours


'''

def format_time(hours, minutes):
    return f'{hours:02d}:{minutes:02d}'

def time_of_day(minutes):
    minutes_per_day = 1440
    minutes_per_hour = 60

    while minutes < 0:
        minutes += minutes_per_day

    minutes = minutes % minutes_per_day
    hours = minutes // minutes_per_hour
    minutes = minutes % minutes_per_hour

    return format_time(hours, minutes)
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
