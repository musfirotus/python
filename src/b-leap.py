'''Leap Module'''

def leapYear(years):
    if (years % 4) == 0:
        if (years % 100) == 0:
            if (years % 400) == 0:
                print("{0} is a leap years".format(years))
            else:
                print("{0} is not a leap years".format(years))
        else:
            print("{0} is a leap years".format(years))
    else:
        print("{0} is not a leap years".format(years))

leapYear(2020)