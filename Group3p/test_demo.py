import calendar
import datetime
import pytest
def caln(year,month):
    day=calendar.SUNDAY
    mon=calendar.monthcalendar(year,month)
    sundays=sum(1 for x in mon if x[day]!=0)
    return sundays
def keys(n):
    dict={50:"chocolate",20:"pepsi"}
    for n in dict.keys():
        return True
    else:
        return False
def desce(l):
    l.sort(reverse=True)
    return l
def mymin(l):
    l.sort(reverse=True)
    n=len(l)
    return l[n-1]