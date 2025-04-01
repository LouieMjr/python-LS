# Some people believe that Fridays that fall on the 13th day of the month are
# unlucky days. Write a function that takes a year as an argument and returns
# the number of Friday the 13ths in that year. You may assume that the year is
# greater than 1752, which is when the United Kingdom adopted the modern
# Gregorian Calendar. You may also assume that the same calendar will remain in
# use for the foreseeable future.


# inputs: int - year
# outputs: int, representing how many friday the 13ths there are in that year

# input will always been greater than 1752
# same calendar year will be used for the future

# want to get the date for a given year starting with the first month
# want to check how many fridays are in each month
# once that is determine, want to check how many fridays are on the 13th day

# import the datetime module
# declare a count variable, initalized to 0
# iterate 12 times, for 12 months in year
# invoke the datetime function passing in the current year and the current index
# (representing the current month), and 13 as the day
# store result into date variable
# invoke strftime on date variable and with format for getting the current day of the
# week for that day
# if the result is 5, which represents friday, increment count variable by 1

# return count varible once loop is finished

from datetime import date

def friday_the_13ths(year):

    # count = 0
    # for month in range(1, 13):
    #     current_date = date(year, month, 13)
    #     day = current_date.strftime("%w")
    #
    #     if int(day) == 5:
    #         count += 1
    #
    # return count

    return sum([1 for month in range(1, 13)
                  if int(date(year, month, 13)
                         .strftime('%w')) == 5])


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
