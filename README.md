# bot-for-click-on-site
<br>

### Описание
Bot for click on button by site. Because always clicked on buttons is tired of it. This is example code for automatization operation by auth in sites.</p>
<hr>

# Основное
## Задача
<p>Создать алгоритм для авторизации на сайтах и далее реализация логики на самом сайте, как автоматизация процесса входа после того как сотрудник пришел на рабочее место.</p>
<p>Задача включает три сайта: Bitrix24, GitLab, Passwork.</p>
<p>Авторизацию можно пройти только один раз при первом открытии, а дальнейшая авторизация происходит за счет файлов cookies записаных в файлах проекта.</p>
<hr>

## Основные действия
<ol>
    <li>Запуск webdriver;</li>
    <li>Открытие сайта;</li>
    <li>Авторизация;</li>
    <li>Дальнейшие действия на сайте.</li>
</ol>
<hr>

## Требования
<ol>
    <li>Модульная реализация;</li>
    <li>Работа с каждым сайтом инкапсулирована в одноименном модуле;</li>
    <li>Простое добавление сайта при добавлени модуля в файл mail.py.</li>
</ol>
<hr>


# Pro-code
### Про множество условий в action для bitrix
<p>Условия необходимы для разделения логики работы "перерыв/продолжить" и "завершить рабочий день/ Обеденное время от 13 до 14!</p>
<blockquote>
    <p>Если время не обеденное, то проверяется "начать" или "закончить" рабочий день</p>
    <p>То есть подразумевается, что дефолтное состояние это - обед</p>
</blockquote>
<p>Всего возможно четыре поведения</p>
<ol>
    <li>
        <b>Boot on break work</b>:
        <br>
        example time = 12:58 - 9 < 12 <= 13 and 12 < 14 and 12 < 18
        <br>
        "true" and "true" and "true" and "true"
        <br>
        true
    </li>
    <li>
        <b>Boot on continue work</b>:
        <br>
        example time = 14:02 - 9 < 14 <= 13 and 14 <= 14 and 13 < 18
        <br>
        "true" and "true" and "true" and "true"
        <br>
        true
    </li>
    <li>
        <b>Don't work</b>:
        <br>
        example time = 09:18 - 9 < 9 <= 13 and 9 <= 14 and 9 < 18
        <br>
        "false" and "false" and "false" and "true"
        <br>
        false - less hour start dinner work, but more hour start work
    </li>
    <li>
        <b>Don't work</b>:
        <br>
        example time = 14:58 - 9 < 14 <= 13 and 14 <= 14 and 14 < 18
        <br>
        "true" and "false" and "false" and "true"
        <br>
        false - more hour ended dinner work
    </li>
    <li>
        <b>Don't work</b>:
        <br>
        example time = 18:18 - 9 < 18 <= 13 and 14 <= 14 and 18 < 18
        <br>
        "true" and "false" and "false" and "false"
        <br>
        false - more hour ended dinner work but more hour end work
    </li>
</ol>
