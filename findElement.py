# -*- coding: utf-8 -*-

# Функция для рекурсивного ожидания элемента
def wait_for_element(selector):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        )
        write_in_log("Элемент с селектором {} найден\n".format(selector))

        return element
    except:
        print("Element not find. Wait...")
        return wait_for_element(selector)