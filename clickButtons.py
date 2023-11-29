# -*- coding: utf-8 -*-

from findElement import wait_for_element
from writeLog import write_in_log
from dateAndTime import getDatetime

# В селекторы передаются полное название селектора
# Пример, если у блока класс "ui-btn ui-btn-icon-pause tm-btn-pause", а пытаешься найти по "tm-btn-pause", то элемент не будет найден

button_css_selector_end_work_day = '[class*="ui-btn-icon-stop"]' # first button - first step
button_css_selector_end_in_popup_work_day = '[class*="popup-window-button"]' # second button - second step

button_css_selector_continue_work_day = '[class*="ui-btn-icon-start"]'

# Ждем, пока кнопка "продолжить / перерыв" загрузится
button_css_selector = '[class*="tm-btn-pause"]' if getDatetime('minute') != 18 else '[class*="tm-btn-start"]'

def set_break_or_continue_work():
    button = wait_for_element

    # Продолжение рабочего дня
    write_in_log("Нажал на кнопку {}\n".format(button_css_selector_continue_work_day))
    button = login_button = wait_for_element(button_css_selector_continue_work_day)
    button.click()

# TODO: дописать!
# TODO: получить селектор!
def set_start_work():
    print("Element not find. Wait...")


def set_end_work():
    button = wait_for_element(button_css_selector_end_work_day)
    write_in_log("Нажал на кнопку {}\n".format(button_css_selector_end_work_day))
    button.click()

    button_in_popup = login_button = wait_for_element(button_css_selector_end_in_popup_work_day)
    write_in_log("Нажал на кнопку {}\n".format(button_css_selector_end_in_popup_work_day))
    button_in_popup.click()