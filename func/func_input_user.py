from func.func_window import createWindow


def getUserMessageWindow(title):
    createWindow(title)


def getUserMessageInput(prompt="Введите что-то:"):
    message = input(f"\033[3;32m\u21E8\033[0m {prompt} ")
    return message
