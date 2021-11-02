from django.shortcuts import render
from datetime import datetime
import calendar

def load_calendar(request):
    print('load')
    return render(request, 'calendar.html', {'days':load()})


def load():
    year = datetime.now().year
    print('year -> {0}'.format(year))
    month = datetime.now().month
    print('month -> {0}'.format(month))    
    monthrange = calendar.monthrange(year, month)    
    print('monthrange -> {0}'.format(monthrange))

    firstday = monthrange[0] + 1
    lastday = monthrange[1] + 1

    days = []

    for i in range (firstday, lastday):
        print('day -> {0} month -> {1}'.format(i, month))
        newdate = '{0}/{1}/{2} 00:00:00'.format(i, month, year)
        print('newdate -> {0}'.format(newdate))
        date_time_obj = datetime.strptime(newdate, '%d/%m/%y %H:%M:%S')
        days.append('{0}/{1}'.format(i, month))
        print(date_time_obj.strftime('%A'))
    return days