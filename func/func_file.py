import os
from func.func_log import writeInLog


def checkExistFileOrDir(path_to_file_or_dir, is_dir=True):
    is_exist = os.path.exists(path_to_file_or_dir)

    writeInLog(f"{'Папка' if is_dir else 'Файл'}: "
               f"{ path_to_file_or_dir } "
               f"{'уже существует!' if is_exist else 'не существует!'}"
    )

    return is_exist


def createFileOrDir(path_to_file_or_dir, is_dir=True):
    # Проверяем наличие файла
    if not checkExistFileOrDir(path_to_file_or_dir):
        # Создаем файл, если его нет
        open(path_to_file_or_dir, "w").close()
        writeInLog(f"{'Папка' if is_dir else 'Файл'}: { path_to_file_or_dir } создан!")


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

