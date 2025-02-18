'''
Write a function that takes a floating point number representing an angle
between 0 and 360 degrees and returns a string representing that angle in
degrees, minutes, and seconds. You should use a degree symbol (°) to represent
degrees, a single quote (') to represent minutes, and a double quote (") to
represent seconds. There are 60 minutes in a degree, and 60 seconds in a
minute.

Note: You can use the following constant to represent the degree symbol:
'''
DEGREE = "\u00B0"

'''
input: floating point number
output: string

explicit rules:
returning a string representing that angle in degrees, minutes, and seconds
- use a degrees symbol to represent degrees
- a single quote to represent minutes
- a double quote to represent seconds
- there are 60 minutes in a degrees
- there are 60 seconds in a minute

implicit rules:
if there is a whole number, that number is represented in degress
- example: input of 30 would be represented as 30° with 0min and 0 sec

- 76.73 would be represented a 76° for the degrees. .73 is not a full degree so
  we need to find out what percentage of 1 degree that is and apply it to the
  minutes. Then whatever minutes is left over will be represented as the
  seconds. 
  Example: if there 43.8 minutes - 43 would be the minutes and we would need to
  multiply .8 by 60 to get the seconds

Data stucture:
list
string


Algo:
if input is a whole number, 
return string with whole number as degrees and minutes and seconds 
as double zeros

if input is a float,
separate the whole number from the decimal number - could use list for this
- use whole number as the degrees and 
- figure out minutes and seconds using the decimal number

get decimal from list, divide 1 degree by decimal = store that result
if result is a decimal
    two options here:
    1. separate whole number from decimal using a list OR
    subtract the whole number from itself, which will leave you with a decimal.
    The whole number is your minutes,
    Then multiply decimal left over by 60 (seconds) this gives you your seconds


return an f string using the aboves results in the correct order


'''
# def separate_decimal_from_whole_number(decimal):
#     separated_by_decimal = str(decimal).split('.')
#     separated_by_decimal[1] = '.' + separated_by_decimal[1]
#     return [int(separated_by_decimal[0]), float(separated_by_decimal[1])]

def add_zero(number):
    num_string = str(number)
    if len(num_string) < 2:
        return '0' + num_string

    return num_string

def dms(number):
    # ONE_DEGREE = 1
    MINUTES_PER_DEGREE = 60
    SECONDS_PER_MINUTE = 60
    SECONDS_PER_DEGREE = MINUTES_PER_DEGREE * SECONDS_PER_MINUTE
    MINUTES_SYMBOL = "'"
    SECONDS_SYMBOL = '\"'

    full_circle = 360
    if number < 0:
        if number < -360:
            number = full_circle - abs(number + full_circle)
        else:
            number = full_circle + number

    if number > 360:
        number = number - full_circle


    int_degrees = int(number)
    minutes = int((number - int_degrees) * MINUTES_PER_DEGREE)
    seconds = int((number - int_degrees - (minutes / MINUTES_PER_DEGREE)) *
                                                            SECONDS_PER_DEGREE)

    minutes = add_zero(minutes)
    seconds = add_zero(seconds)

    msg = (f"{int_degrees}{DEGREE}"
          f"{minutes}{MINUTES_SYMBOL}"
          f"{seconds}{SECONDS_SYMBOL}")

    return msg
    #
    # if type(number) == int:
    #     return f'{number}{DEGREE}00{MINUTES_SYMBOL}00{SECONDS_SYMBOL}'
    #
    # degree, partial_degree = separate_decimal_from_whole_number(number)

    # percentage_of_degree = round(ONE_DEGREE / partial_degree, 2)
    # minutes = round(MINUTES_PER_DEGREE / percentage_of_degree, 2)
    #
    # minutes, partial_minutes = separate_decimal_from_whole_number(minutes)
    #
    # seconds = round(SECONDS_PER_MINUTE * partial_minutes)
    #
    # minutes = add_zero(minutes)
    # seconds = add_zero(seconds)
    #
    # return f'{degree}{DEGREE}{minutes}{MINUTES_SYMBOL}{seconds}{SECONDS_SYMBOL}'

print(dms(-1) == "359°00'00\"")
print(dms(400) == "40°00'00\"")
print(dms(-40) == "320°00'00\"")
print(dms(-420) == "300°00'00\"")
print(dms(30) == "30°00'00\"")
print(dms(-30) == "330°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
