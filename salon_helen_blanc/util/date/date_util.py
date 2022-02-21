from datetime import datetime
import calendar

DD_MM_YYYY_HH_MI_SS_SLASH = '%d/%m/%Y %H:%M:%S'
DD_MM_YYYY_SLASH = '%d/%m/%Y'
DD_MM_SLASH = '%d/%m'
MM_YYYY_SLASH = '%m/%Y'
DD_MM_YYYY_HH_MI_SS = '%d-%m-%Y %H:%M:%S'

class Date:
    def __init__(self, day, month, year, hour, minute, second):
        newdate = create_date_DD_MM_YYYY_HH_MI_SS_SLASH(day, month, year, hour, minute, second)
        self.date = newdate
        self.day = newdate.day
        self.month = newdate.month
        self.year = newdate.year
        self.hour = newdate.hour
        self.minute = newdate.minute
        self.second = newdate.second
        self.month_of_year = month_of_year(newdate.month)
        self.day_of_week = day_of_week(newdate.weekday())
        self.dd_mm_yyyy = newdate.strftime(DD_MM_YYYY_SLASH)
        self.dd_mm_yyyy_hh_mi_ss = newdate.strftime(DD_MM_YYYY_HH_MI_SS_SLASH)
        self.dd_mm = newdate.strftime(DD_MM_SLASH)
        self.mm_yyyy = newdate.strftime(MM_YYYY_SLASH)

    def to_json(self):
        return {
                'month': self.month,
                'year': self.year,
                'day': self.day,
                'hour': self.hour,
                'minute': self.minute,
                'second': self.second,
                'month_of_year': self.month_of_year,
                'day_of_week': self.day_of_week,
                'dd_mm_yyyy': self.dd_mm_yyyy,
                'dd_mm_yyyy_hh_mi_ss': self.dd_mm_yyyy_hh_mi_ss,
                'dd_mm': self.dd_mm,
                'mm_yyyy': self.mm_yyyy
        }

def day_of_week(number_day):
    name_day_for_week = ""
    if number_day == 0:
        name_day_for_week = "Lunes"
    elif number_day == 1:
        name_day_for_week = "Martes"
    elif number_day == 2:
        name_day_for_week = "Miércoles"
    elif number_day == 3:
        name_day_for_week = "Jueves"
    elif number_day == 4:
        name_day_for_week = "Viernes"
    elif number_day == 5:
        name_day_for_week = "Sábado"
    elif number_day == 6:
        name_day_for_week = "Domingo"
    return name_day_for_week

def month_of_year(number_month):
    name_month_for_year = ""
    if number_month == 1:
        name_month_for_year = "Enero"
    elif number_month == 2:
        name_month_for_year = "Febrero"
    elif number_month == 3:
        name_month_for_year = "Marzo"
    elif number_month == 4:
        name_month_for_year = "Abril"
    elif number_month == 5:
        name_month_for_year = "Mayo"
    elif number_month == 6:
        name_month_for_year = "Junio"
    elif number_month == 7:
        name_month_for_year = "Julio"
    elif number_month == 8:
        name_month_for_year = "Agosto"
    elif number_month == 9:
        name_month_for_year = "Septiembre"
    elif number_month == 10:
        name_month_for_year = "Octubre"
    elif number_month == 11:
        name_month_for_year = "Noviembre"
    elif number_month == 12:
        name_month_for_year = "Diciembre"
    return name_month_for_year

def text_to_date(text_date, format):
    newdate = datetime.strptime(text_date, format)
    return newdate

def text_to_date_DD_MM_YYYY_HH_MI_SS_SLASH(text_date):
    return text_to_date(text_date, DD_MM_YYYY_HH_MI_SS_SLASH)

def text_to_date_DD_MM_YYYY_HH_MI_SS(text_date):
    return text_to_date(text_date, DD_MM_YYYY_HH_MI_SS)

def create_date_DD_MM_YYYY_HH_MI_SS_SLASH(day, month, year, hour, minute, second):
    newdate = '{0}/{1}/{2} {3}:{4}:{5}'.format(day, month, year, hour, minute, second)
    return text_to_date_DD_MM_YYYY_HH_MI_SS_SLASH(newdate)

def create_date_DD_MM_YYYY_SLASH(day, month, year):
    return create_date_DD_MM_YYYY_HH_MI_SS_SLASH(day, month, year, 0, 0, 0)

def create_date(day, month, year, hour, minute, second):
    return Date(day, month, year, hour, minute, second)