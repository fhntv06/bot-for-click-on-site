# -*- coding: utf-8 -*-
import sys
import time
from datetime import datetime


def getDateTimeNow(value=''):
    # Получаем текущее время
    current_datetime = datetime.now()  # момент запуска кода

    values = {
        'day': current_datetime.day,
        'month': current_datetime.month,
        'year': current_datetime.year,
        'hour': current_datetime.hour,
        'minute': current_datetime.minute,
        'second': current_datetime.second,
        'all': [
            current_datetime.day,
            current_datetime.month,
            current_datetime.year,
            current_datetime.hour,
            current_datetime.minute,
            current_datetime.second,
        ]
    }

    return values.get(value)


def getHourInMinutes(hour='hour'):
    forming_minutes = hour if isinstance(hour, (int, float)) else getDateTimeNow('hour')
    return forming_minutes * 60


def getCtime():
    return time.ctime()


def getAllDateAndTime(state=False):
    day, month, year, hour, minute, second = getDatetimeCorrect('all')

    return f'{day}{month}{year}_{hour}{minute}{second}' \
        if state \
        else f'{day}/{month}/{year} {hour}:{minute}:{second}'


def dispenseValue(value):
    return f'0{value}' if value < 10 else value


def formingCorrectStringDate(value):
    return list(map(dispenseValue, value)) if type(value) == list else dispenseValue(value)


def getDatetimeCorrect(selector):
    return formingCorrectStringDate(
        getDateTimeNow(selector)
    )


def getDatetime(selector):
    return getDateTimeNow(selector)
