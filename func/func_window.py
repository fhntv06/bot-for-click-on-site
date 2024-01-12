import tkinter as tk
import keyboard


from func.func_log import writeInLog
from func.func_driver import quitDriver


def getEntryUser(entry, message):
    writeInLog(f"Пользователь ввел в поле ввода: '{ entry.get() }'")
    message = entry.get()


def createWindow(title='Введите название сайта', callback=None):
    message = ''

    # Создаем главное окно
    window = tk.Tk()
    window.title(title)

    writeInLog(f'Создалось окно с заголовком { title }')

    entry = createEntry(window)

    # Создаем кнопку для отправки
    submit_button = tk.Button(window, text="Ввести", command=lambda: getEntryUser(entry, message))
    submit_button.pack()

    # Создаем переменную для сообщения
    message_var = tk.StringVar(value='')

    # Виджет для вывода сообщения
    message_label = tk.Label(window, textvariable=message_var)
    message_label.pack()

    # Запускаем главный цикл событий
    window.mainloop()

    return message


def createEntry(window):
    writeInLog(f'Создалось поле ввода')

    # Создаем виджет Entry для ввода текста
    entry = tk.Entry(window, width=50, font=('Helvetica', 16), fg="black", bg="white")
    entry.pack(pady=10)

    return entry


def exitApp(driver):
    writeInLog('Для выхода нажмите Esc')

    def on_key_event(e):
        if e.event_type == keyboard.KEY_UP:
            quitDriver(driver)

    # Зарегистрируем функцию обратного вызова
    keyboard.hook(on_key_event)

    # Бесконечный цикл для ожидания событий
    keyboard.wait('esc')  # Ждем, пока не будет нажата клавиша Esc

