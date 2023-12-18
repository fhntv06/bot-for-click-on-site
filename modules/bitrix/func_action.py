# -*- coding: utf-8 -*-
import sys
import time

from func.func_work_with_element import findElementAndClick
from func.func_datetime import getHourInMinutes
from func.func_log import writeInLog
from variables.time import time_start_work, time_end_work, time_start_dinner_break, \
    time_end_dinner_break

time_now = getHourInMinutes()

# Проверка на time_start_work добавлена для того,
# чтобы учитывать начало рабочего дня т.к. time_start_work < time_start_dinner_break

state_break_or_continue_work = (
        time_start_dinner_break <= time_now <= time_end_dinner_break
        and time_now < time_end_work
)

# В селекторы передаются полное название селектора
# Пример, если у блока класс "ui-btn ui-btn-icon-pause tm-btn-pause",
# а пытаешься найти по "tm-btn-pause", то элемент не будет найден

button_css_selector_start_work_day = '[class*="ui-btn-icon-start"]'

button_css_selector_end_work_day = '[class*="ui-btn-icon-stop"]'  # first button - first step
button_css_selector_end_in_popup_work_day = '[class*="popup-window-button"]'  # second button - second step

button_css_selector_continue_work_day = '[class*="ui-btn-icon-start"]'
button_css_selector_break_work_day = '[class*="ui-btn-icon-pause"]'


def work_time_man_block(driver):
    time_man_block_selector = '[id*="timeman-"]'
    findElementAndClick(driver, time_man_block_selector)


def set_switch_states_work(driver):
    work_time_man_block(driver)
    # Перерыв / Продолжение рабочего дня

    if state_break_or_continue_work:
        set_break_or_continue_work(driver)
    else:
        set_toggle_work(driver)


def set_break_or_continue_work(driver):
    state = time_now <= time_start_dinner_break

    button_css_selector = (
        button_css_selector_break_work_day if state else button_css_selector_continue_work_day
    )

    text_log = (
        'Попытка прервать рабочий день!' if state else 'Попытка продолжить рабочий день!'
    )

    writeInLog(text_log)
    findElementAndClick(driver, button_css_selector)  # перерыв или продолжить

    time.sleep(2)


def set_toggle_work(driver):
    if time_end_dinner_break < time_now < time_end_work:
        writeInLog('Время окончания рабочего дня еще не наступило!')
        return
    # Начало рабочего дня / Завершение рабочего дня
    # Ожидаемое поведение:
    #   true - start work
    #   false - end work
    #   else false - time not end work

    state_end_or_start_work = time_start_work <= time_now < time_start_dinner_break

    button_css_selector = (
        button_css_selector_start_work_day if state_end_or_start_work
        else button_css_selector_end_work_day
    )

    text_log = 'Попытка начать рабочий день!' if state_end_or_start_work else 'Попытка закончить рабочий день!'

    writeInLog(text_log)
    findElementAndClick(driver, button_css_selector)

    if not state_end_or_start_work:
        findElementAndClick(driver, button_css_selector_end_in_popup_work_day)

    time.sleep(5)
