# -*- coding: utf-8 -*-
import sys
import re

from selenium.common import TimeoutException

from func.func_input_user import getUserMessageInput
from func.func_log import writeInLog
from func.func_screenshot import makeScreenshot
from func.func_driver import initDriver
from func.func_site import openSite, timeoutException, formingSite
from func.func_window import exitApp


driver = initDriver()
writeInLog('Запуск приложения: Screenshot on site')

# TODO: Пользователь должен иметь возможность вводить название сайтов не ограниченное количество раз
#   - продление timeout, чтобы не закрывать программу

name_site = ''


def applicationSupportsSecureRestorableState(self):
    return True


def action():
    global name_site

    name_site = getUserMessageInput('Введите сайт, с которого хотите получить скриншот:')

    exitApp(driver)

    try:
        openSite(driver, name_site)

    except TimeoutException:  # отработка только для двух раз ввода имени сайта
        timeoutException(formingSite(name_site))

    except Exception as ex:
        string = str(ex)
        match = re.search(r'e=([^&]+)', string)
        result = match.group(1)

        writeInLog(f"Сайт {formingSite(name_site)} не найден! Ошибка {result}", True)

        action()

    makeScreenshot(driver, name_site)


action()
