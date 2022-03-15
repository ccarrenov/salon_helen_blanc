from django.shortcuts import render
from datetime import datetime
import calendar
from salon_helen_blanc.util.date.date_util import Years, create_date, Months
import json

def load_calendar(request):
    current_month = 0
    try:
        month = int(request.GET['month'])
        current_month = month
    except Exception as e:
        print(e)
        month = datetime.now().month
        current_month = month
    try:
        year = int(request.GET['year'])
    except Exception as e:
        print(e)
        year = datetime.now().year
    print('month -> {0}'.format(month))
    print('year -> {0}'.format(year))

    return render(request, 'calendar.html', {'days':load(year, month), 'months': months(), 'current_month': current_month, 'years': years(), 'current_years': current_years()})


def load(year, month):
    #year = datetime.now().year
    #print('year -> {0}'.format(year))
    #month = datetime.now().month
    #print('month -> {0}'.format(month))    
    monthrange = calendar.monthrange(year, month)    
    print('monthrange -> {0}'.format(monthrange))

    firstday = monthrange[0]
    if firstday == 0:
        firstday = 1
    lastday = monthrange[1] + 1

    days = []
    months = Months()

    for i in range (firstday, lastday):
        print('day -> {0} month -> {1}'.format(i, month))
        newdate = create_date(i, month, year, 0, 0 , 0)
        days.append(newdate)
        print(newdate.to_json())
    return days

def months():
    return Months().months

def current_month():
    return datetime.now().month

def years():
    return Years().years

def current_years():
    return datetime.now().year