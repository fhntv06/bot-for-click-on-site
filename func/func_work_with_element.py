# -*- coding: utf-8 -*-
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from func.func_log import writeInLog, writeLogAndExit
from variables.common import timeout

attempt = 0


def findElement(driver, selector, mode=''):
    values_by = By.ID if mode == 'id' else By.CSS_SELECTOR

    writeInLog(f"Ищу {selector} ...")

    element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((values_by, selector))
    )

    return element


def visibleElement(driver, selector):
    element = findElement(driver, selector)
    return element.is_displayed()


# Функция для рекурсивного ожидания элемента
def exeption(driver, selector, mode):
    global attempt
    if attempt < 2:
        attempt += 1
        findElementException(driver, selector, mode)
    else:
        writeLogAndExit(f"{selector} не найден")


def findElementException(driver, selector, mode=''):
    try:
        return findElement(driver, selector, mode)

    except:
        writeLogAndExit(f"{selector} не найден. Ищу дальше!")
        exeption(driver, selector, mode)


def findElementAndInsert(driver, selector, value):
    element = findElementException(driver, selector)

    try:
        element.clear()
        element.send_keys(value)
    except:
        writeLogAndExit(f"Элемент { selector } не в зоне видимости")

    writeInLog(f"Ввел значение: { value } в { selector }\n")
    time.sleep(1)


def findElementAndClick(driver, selector):
    element = findElementException(driver, selector)
    try:
        # Проверяем, что кнопка видима на странице
        if element.is_displayed():
            time.sleep(1)
            element.click()
    except:
        writeLogAndExit(f"Элемент { selector } не в зоне видимости")

    writeInLog(f"Нажал на кнопку { selector }\n")
    time.sleep(1)
