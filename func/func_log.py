# -*- coding: utf-8 -*-
import sys
from func.func_datetime import getAllDateAndTime

# Путь для создания файла по этому пути
from variables.common import file_log


def writeInLog(message, is_error=False):
    correct_message = f"\033[1;30m\u274C\033[0m\033[1;31m {message}\033[40m"\
        if is_error\
        else f"\033[3;32m\u21E8\033[0m {message}"

    symbol = '❌' if is_error else '⇨'

    with open(file_log, "a") as file:
        print(correct_message + '\n')
        file.write(symbol + ' ' + message + '\n')


def writeLogAndExit(message):
    text_end_script = f"Остановил выполнение скрипта в {getAllDateAndTime()}"
    writeInLog(message, True)
    writeInLog(text_end_script, True)
    sys.exit()

