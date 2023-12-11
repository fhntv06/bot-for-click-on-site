# -*- coding: utf-8 -*-
import sys
from func.func_log import writeInLog
from func.func_datetime import getAllDateAndTime
from func.func_file import fileWork
from func.func_screenshot import makeScreenshot
from func.func_driver import initDriver, quitDriver
from func.func_site import openSite, getNameSite
from variables.common import timeout
from func.func_input_user import getUserMessageInput
# from func.func_NSApplicationDelegate import NSApplicationDelegate

# NSApplicationDelegate()
writeInLog('Запуск приложения: Screenshot on site')

message = ''
name_site = getNameSite('Введите сайт, с которого хотите получить скриншот:')
driver = initDriver()

# TODO: Добавить удержание пользователя, чтобы не закрывать программу, а давать ему снова и снова вводить название сайта
# TODO: Добавить возможность пробление timeout, чтобы не закрывать программу

def action():
    try:
        openSite(driver, name_site)
        makeScreenshot(driver, name_site)

    except TimeoutException:
        name_site = timeoutException(forming_site)
        makeScreenshot(driver, name_site)

    except Exception as ex:
        writeInLog(f"{ex}", True)
        getNameSite('Введите другой сайт: ')

try:
    action()
except Exception as ex:
    writeInLog(f"{ ex }", True)
finally:
    quitDriver(driver)
