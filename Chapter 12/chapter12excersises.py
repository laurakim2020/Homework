#Problema
import calendar
cal = calendar.TextCalendar()      # Create an instance
cal.pryear(2012)

#Problem b
import calendar
cal=calendar.TextCalendar(firstweekday=3)
cal.pryear(2012)

#Problem c
import calendar
cal=calendar.TestCalendar(6)
cal.prmonth(2018,2)

#Problem d
import calendar
d = calendar.LocaleTextCalendar(6, "KOREAN")
d.pryear(2012)

import calendar
d = calendar.LocaleTextCalendar(6, "PAWNEE")
d.pryear(2012)

#Problem e
print(calendar.isleap(12))
#It expects a year. It returns true for leap years and false for non-leap years. It is a boolean function.

#How many functions are in math module? 47 (according to Leo in section F)

#Problem2
import math
myvar = math.floor(78.89)
print(myvar)
myvar = math.ceil(78.89)
print(myvar)

# What does math.ceil do? What about math.floor? math.floor rounds down. math.ceil rounds up

# Describe how we have been computing the same value as math.sqrt without using the math module.
mysq = 16 ** (1/9)
print(mysq)
mysq = mathsqrt(16)
print(mysq)

#What are the two data constants in the math module? 'e' & 'pi'

#What does deepcopy do? In which exercises from last chapter would deepcopy have come in handy? Deepcopy returns a deep copy of x. It would come in handy for exercises that you didn't have to solve dealing with object reference since there is no answer.

#Run namespace_test.py. What happens? Why? namespace_test.py prints My name is __main__ because

#Run mymodule1.py and namespace_test.py again. In which case do you see the new print statement? mymodule1