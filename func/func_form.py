import sys
import time
from func.func_cookies import dumpCookies
from func.func_work_with_element import (
    findElementException,
    findElementAndInsert,
    findElementAndClick,
    visibleElement
)
from func.func_log import writeInLog
from func.func_cookies import loadCookies, checkValidCookies


def authentication(driver, object):
    file_cookies = object['file_cookies']
    login = object['login']
    password = object['password']
    selectors = object['selectors']

    # Вводим данные в поля формы
    findElementAndInsert(driver, selectors[0], login)
    findElementAndInsert(driver, selectors[1], password)

    # Нажимаем на кнопку входа
    findElementAndClick(driver, selectors[2])

    dumpCookies(driver, file_cookies)


def checkFormFilled(driver, field_selectors):
    try:
        for field_selector in field_selectors:
            field = findElementException(driver, field_selector)

            if not field.get_attribute("value"):
                writeInLog(f'Поле {field_selector} не заполнено!')
                return False

        return True

    except Exception as e:
        writeInLog(f"Ошибка при проверке заполнения формы: {e}")
        return False


def formWork(driver, object):
    selectors = object['selectors']
    field_selectors = [selectors[0], selectors[1]]
    file_cookies = object['file_cookies']

    writeInLog("Начало работы с формой!")

    # fk cookie about pages refresh
    # if checkValidCookies(file_cookies):
    #     loadCookies(driver, file_cookies)
    #     writeInLog("Форму прошел!\n")
    #     return
    #
    # else:
    #     authentication(driver, object)
    #
    # # checked error when cookie is actual and page refresh but form don't coming
    # if not visibleElement(driver, selectors[2]) and not checkFormFilled(driver, field_selectors):
    #     authentication(driver, object)

    authentication(driver, object)

    writeInLog("Форму прошел!\n")
