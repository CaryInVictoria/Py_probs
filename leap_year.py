def leap_year(y):
    if y % 400 == 0:
        return (True)
    if y % 100 == 0:      
        return (False) 
    if y % 4 == 0:
        return True 
    return False

or
def leap_year(y):
    return y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)

def report_leap_year(y):
    if leap_year(y):
        print(str(y) + ' is a leap year')
    else:
        print(str(y) + ' is not a leap year')

report_leap_year(2000) # => 2000 is a leap year
report_leap_year(1900) # => 1900 is not a leap year
report_leap_year(2012) # => 2012 is a leap year
report_leap_year(2013) # => 2013 is not a leap year
