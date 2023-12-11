import sys
import pickle
import time
import os
import datetime
from func.func_file import deleteFileOrDir, checkExistFileOrDir
from func.func_log import writeInLog
from variables.time import time_live_cookie


def loadCookies(driver, file_cookies):
    for cookie in pickle.load(open(file_cookies, 'rb')):
        driver.add_cookie(cookie)

    writeInLog(f"Cookie загружены!")
    time.sleep(1)
    driver.refresh()


def checkValidCookies(file_cookies=None):
    today_datetime = datetime.datetime.now()

    if file_cookies is None:
        return False

    # Получение времени создания файла (только на некоторых системах поддерживается)
    try:
        writeInLog(f"Проверка валидности времени создания файла cookie: { file_cookies }!")

        creation_time = os.path.getctime(file_cookies)
        creation_datetime = datetime.datetime.fromtimestamp(creation_time)

        writeInLog(f"Дата создания файла: { creation_datetime }")

        # Получение разницы между часами обоих дат
        time_difference = today_datetime - creation_datetime
        hours_difference = time_difference.total_seconds() / 3600

        cookie_is_live = hours_difference < time_live_cookie

        writeInLog(f"Cookie актуальны") if cookie_is_live else writeInLog(f"Время жизни cookie вышло")

        return cookie_is_live

    except OSError as ex:
        writeInLog(f"Время создания файла не поддерживается на данной системе: { ex }", True)
        return False


def dumpCookies(driver, file_cookies):
    if checkExistFileOrDir(file_cookies):
        deleteFileOrDir(file_cookies)

    pickle.dump(driver.get_cookies(), open(file_cookies, 'wb'))  # Запись в куки при первом входе
    writeInLog(f"Файл cookie создан и перезаписан!")
