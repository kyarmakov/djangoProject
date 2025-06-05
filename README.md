Простое Django-приложение для блога.

Порядок запуска:

1. Открыть консоль (командную строку на Windows) и клонировать проект ```git clone https://github.com/kyarmakov/djangoProject```
2. Перейти в папку проекта ```cd djangoProject```
3. Создать виртуальное окружение для избежания конфликтов версий ```python -m venv .venv``` для Windows и ```python3 -m venv .venv``` для Linux и Mac.
4. Активировать виртуальное окружение. Для Windows ```.venv\Scripts\activate``` . Для Linux/Mac ```source .venv/bin/activate```
5. Выполнить команду ```pip install -r requirements.txt``` для установки зависимостей.
6. Выполнить команду ```python manage.py runserver```

HTML:
<br>
Все посты - ```http://localhost:8000/```
<br>
Создать пост - ```http://localhost:8000/create-post/```
<br>
Один пост - ```http://localhost:8000/post/1/```

АПИ:
<br>
Список постов - ```http://localhost:8000/api/posts/```
<br>
Один пост - ```http://localhost:8000/api/posts/1/```
<br>
Создать пост - ```http://localhost:8000/api/posts/1/comments```
