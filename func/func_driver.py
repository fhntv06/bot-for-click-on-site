from selenium import webdriver
from func.func_datetime import getAllDateAndTime
from func.func_log import writeInLog
from func.func_file import fileWork


def initDriver():
    fileWork()
    # Создание экземпляра драйвера
    return webdriver.Firefox()


def quitDriver(driver):
    separator = '============================== The End ==============================\n'

    driver.close()

    writeInLog("\nЗакрыл браузер!")

    driver.quit()

    writeInLog(f'Завершил работу в { getAllDateAndTime() }\n\n{ separator }')

