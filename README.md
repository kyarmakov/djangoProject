Простое Django приложение для блога.

Порядок запуска:

1. Открыть консоль (командную строку на Windows) и клонировать проект git clone https://github.com/kyarmakov/djangoProject
2. Перейти в папку проекта cd djangoProject
3. Создать виртуальное окружение для избежания конфликтов версий python -m venv .venv для Windows и python3 -m venv .venv для Linux и Mac.
4. Активировать виртуальное окружение. Для Windows .venv\Scripts\activate . Для Linux/Mac source .venv/bin/activate
5. Выполнить команду pip install -r requirements.txt для установки зависимостей.
6. Выполнить команду python manage.py runserver

HTML:
Все посты - http://localhost:8000/
Создать пост - http://localhost:8000/create-post/
Один пост - http://localhost:8000/post/1/

АПИ:
Список постов - http://localhost:8000/api/posts/
Один пост - http://localhost:8000/api/posts/1/
Создать пост - http://localhost:8000/api/posts/1/comments
