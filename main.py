# -*- coding: utf-8 -*-
import sys
import time

from auth.data import data
from func.func_driver import initDriver, quitDriver
from func.func_site import openSite
from func.func_form import formWork
from func.func_log import writeInLog


writeInLog('Запуск приложения: Authterization')


driver = initDriver()  # init driver


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
finally:
    quitDriver(driver)
