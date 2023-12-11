import os
from func.func_log import writeInLog
from func.func_datetime import getAllDateAndTime
from variables.common import file_log


def checkExistFileOrDir(path_to_file_or_dir, type='f'):
    is_exist = os.path.exists(path_to_file_or_dir)

    if is_exist:
        writeInLog(f"{'Папка' if type == 'd' else 'Файл'}: { path_to_file_or_dir } уже существует!")
    else:
        writeInLog(f"{'Папка' if type == 'd' else 'Файл'}: { path_to_file_or_dir } не существует!")

    return is_exist


def createFileOrDir(path_to_file_or_dir, type='f'):
    # Проверяем наличие файла
    if not checkExistFileOrDir(path_to_file_or_dir):
        # Создаем файл, если его нет
        writeInLog(f"{'Папка' if type == 'd' else 'Файл'}: { path_to_file_or_dir } создан!")
        open(path_to_file_or_dir, "w").close()


def deleteFileOrDir(path_to_file_or_dir):
    try:
        os.remove(path_to_file_or_dir)
        writeInLog(f"Файл { path_to_file_or_dir } успешно удален!")
    except FileNotFoundError:
        writeInLog(f"Файл { path_to_file_or_dir } не найден!", True)
    except PermissionError:
        writeInLog(f"Нет разрешения на удаление файла { path_to_file_or_dir }!", True)
    except Exception as e:
        writeInLog(f"Произошла ошибка при удалении файла: { e }!", True)


def fileWork():
    separator = '============================== BOOT ==============================\n'

    # Открываем файл для записи
    with open(file_log, "a") as file:
        # Записываем лог
        writeInLog(f"{ separator }Скрипт запущен в { getAllDateAndTime() }!")

    createFileOrDir(file_log)

