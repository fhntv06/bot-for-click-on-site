# -*- coding: utf-8 -*-
import sys
import time

from auth.data import data
from func.func_driver import initDriver, quitDriver
from func.func_log import writeInLog
from func.func_site import openSite
from func.func_form import formWork


driver = initDriver()  # init driver
writeInLog('Запуск приложения: Authentication')


def action():
    for name, object in data.items():
        action_for_site = object['action']
        link = object['link']

        openSite(driver, link)  # открыть сайт - WORK!
        formWork(driver, object)  # пройти форму
        action_for_site(driver)


try:
    action()
except Exception as ex:
    print(f"\033[31m { ex } \033[0m")

    print(f"🔄 Перезапуск скрипта!")
    action()
finally:
    quitDriver(driver)
