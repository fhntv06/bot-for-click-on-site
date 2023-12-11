from variables.common import timeout
from func.func_log import writeInLog
from func.func_input_user import getUserMessageInput
from func.func_screenshot import makeScreenshot
from selenium.common.exceptions import TimeoutException


def formingSite(name_site):
    return f'https://{ name_site }'


def getNameSite(message_for_user):
    return getUserMessageInput(message_for_user)


def timeoutException(link):
    # Обработка исключения в случае превышения таймаута
    writeInLog(
        f"\033[1;30m\u274C\033[0m Превышено время ожидания ({ timeout } секунд), "
        f"возможно не корректно имя сайта. Сайт по адресу: { link }.", True)

    return getUserMessageInput('Введите другое имя сайта:')


def openSite(driver, link):
    forming_site = formingSite(link)
    driver.set_page_load_timeout(timeout)

    writeInLog(f"Попытка открыть сайт: { forming_site }")

    driver.get(forming_site)

    writeInLog(f"✓ Открыл сайт: { forming_site }")
