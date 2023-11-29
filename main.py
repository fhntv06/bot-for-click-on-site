# -*- coding: utf-8 -*-
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from clickButtons import set_start_work, set_end_work, set_break_or_continue_work
from writeLog import write_in_log
from findElement import wait_for_element
from dateAndTime import getDatetime

getDatetime('minutes')
getDatetime('day')
sys.exit();

print("Начал работу!")
timeout = 20
site = 'https://b24.make.st/company/personal/user/79/tasks/'

# Указываем путь к ChromeDriver
web_driver_url = '/opt/homebrew/bin/chromedriver'

# Получаем драйвер браузера
driver = webdriver.Chrome(web_driver_url)

def workWithSite():
    # Открываем сайт
    driver.get(site)
################ Datetime__End ################
# Проверяем наличие файла
if not os.path.exists("log.txt"):
    # Создаем файл, если его нет
    open("log.txt", "w").close()

# Открываем файл для записи
with open("log.txt", "a") as file:
    # Записываем лог
    write_in_log("\n\n")
    write_in_log("Скрипт выполнен {}/{}/{} в {}:{}:{}\n"
                 .format(getDatetime('day'), getDatetime('month'), getDatetime('year'),
                         getDatetime('hour'), getDatetime('minute'), getDatetime('second'))
                 )


write_in_log("Открываем сайт {}\n".format(site))
write_in_log("\n")

################ Форма ################
# Ждем, пока форма авторизации загрузится
write_in_log("Начало работы с формой!\n")
username_input = wait_for_element('input[name="USER_LOGIN"]')
# Проверяем, что кнопка видима на странице
if username_input.is_displayed():
    password_input = wait_for_element('input[name="USER_PASSWORD"]')
    login_button = wait_for_element('input[type="submit"]')

    # Вводим данные в поля формы
    username_input.send_keys('a.kuskov@make.st')
    password_input.send_keys('-89hjkpZ!;')

    # Нажимаем на кнопку входа
    login_button.click()
else:
    print("Form not visible")


################ Форма ################
timemanBlock = WebDriverWait(driver, timeout).until(
    EC.presence_of_element_located((By.ID, 'timeman-block'))
)
# Проверяем, что кнопка видима на странице
if timemanBlock.is_displayed():
    write_in_log("timeman-block найден\n")
    write_in_log("Форму прошел!\n")
    write_in_log("\n")

    # Нажимаем на кнопку
    timemanBlock.click()
else:
    print("timemanBlock not visible")

# Завершения рабочего дня
if current_time.hour == 9 and current_time.minute < 25:
    set_start_work()

if current_time.hour == 18 and current_time.minute >= 15:
    set_end_work()



driver.quit()
sys.exit();

button = login_button = wait_for_element(button_css_selector) # перерыв и продолжить
# Проверяем, что кнопка видима на странице
if button.is_displayed():
    # Нажимаем на кнопку
    write_in_log("Нажал на кнопку {}\n".format(button_css_selector))
    button.click()
else:
    print("button not visible")

write_in_log("Закрываем браузер\n")
print("Завершил работу!")
# Закрываем браузер
driver.quit()
