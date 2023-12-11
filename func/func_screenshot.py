import os
from func.func_datetime import getAllDateAndTime
from func.func_log import writeInLog, writeLogAndExit
from func.func_file import checkExistFileOrDir


def makeScreenshot(driver, name_file):
    date_and_time = getAllDateAndTime(True)
    dir_screenshots = 'screenshots'
    name_screenshot = '/' + name_file + '_' + date_and_time
    expansion = '.png'

    checkExistFileOrDir(dir_screenshots, 'd')

    path = f"{dir_screenshots}{name_screenshot}{expansion}"

    try:
        driver.get_screenshot_as_file(f'{path}')
        writeInLog(f'Создал скриншот { name_screenshot } в папке { dir_screenshots } ({ path })')

    except:
        writeLogAndExit(f' Cкриншот { name_screenshot } не создан!')
