#Problem1b
import calendar
cal=calendar.TextCalendar(firstweekday=3)
cal.pryear(2012)

#Problem1c
import calendar
cal=calendar.TestCalendar()
print(cal.prmonth(2018,1))

#Problem1d
d = calendar.LocaleTextCalendar(6, "KOREAN")
d.pryear(2012)

d = calendar.LocaleTextCalendar(6, "PAWNEE")
d.pryear(2012)

#Problem1e
>>> from calendar import *
>>> isleap(2012)
True
>>> isleap(2011)
False
#What does it expect as an argument? What does it return as a result? What kind of a function is this? It expects a year inputed. It returns true for leap years and false for non-leap years.


#How many functions are in math module? 35
#What does math.ceil do? What about math.floor? math.ceil returns the smallest integer greater than or equl to x. math.floor returns the largest integer greater than or equal to x.
#Describe how we have been computing the same value as math.sqrt without using the math module. By getting closer to the square root of the start number
#What are the two data constants in the math module? 'e' & 'pi'

#What does deepcopy do? In which exercises from last chapter would deepcopy have come in handy?







