# -*- coding: utf-8 -*-
import sys
from datetime import datetime

################ Datetime__Start ################
# Получаем текущее время
current_datetime = datetime.now()

values = {
    'year': current_datetime.year,
    'month': current_datetime.month,
    'day': current_datetime.day,
    'hour': current_datetime.hour,
    'minute': current_datetime.minute,
    'second': current_datetime.second
}


def getDatetime(selector):
    print("Для {} дата: {}".format(selector, values.get(selector)))
    return values.get(selector)
