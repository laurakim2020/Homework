#b
import calendar
cal=calendar.TextCalendar(firstweekday=3)
cal.pryear(2012)

#c
import calendar
cal=calendar.TestCalendar(6)
cal.prmonth(2018,2)

#d
import calendar
d = calendar.LocaleTextCalendar(6, "PAWNEE")
d.pryear(2012)

#e
print(calendar.isleap(12))
#It expects a year. It returns true for leap years and false for non-leap years. It is a boolean function.

