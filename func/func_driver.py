from selenium import webdriver
from func.func_datetime import getAllDateAndTime
from func.func_log import writeInLog


def boot():
    writeInLog(f"{ '============================== BOOT ==============================' }\n")
    writeInLog(f"Скрипт запущен в { getAllDateAndTime() }!\n")


def initDriver():
    boot()
    writeInLog("Экземпляр драйвера Firefox создан!\n")
    return webdriver.Firefox()


def quitDriver(driver):
    driver.close()

    writeInLog("Закрыл браузер!")

    driver.quit()

    writeInLog(f'Завершил работу в { getAllDateAndTime() }\n')
    writeInLog(f"{ '============================== The End ==============================' }\n")

