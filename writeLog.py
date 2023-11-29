# -*- coding: utf-8 -*-

# Путь для создания файла по этому пути
filelog = 'log.txt'


def write_in_log(message):
    with open(filelog, "a") as file:
        file.write(message)
