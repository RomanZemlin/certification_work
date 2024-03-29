# Платформа торговой сети электроники.

## Установка

1. Убедитесь, что у вас установлен python 3.11 или более новая версия
2. Убедитесь, что у вас установлен PostgreSQL и запущен локальный сервер для базы данных
3. Склонировать репозиторий
4. Создать и активировать виртуальное окружение python -m venv ваша_папка_для_виртуального_окружения
5. Установить зависимости командой pip install -r requirements.txt
6. Создать миграции через python3 manage.py makemigrations и применить их python3 manage.py migrate
7. В файле .env.sample заполнить данные для работы с проектом и переименовать его в .env
8. Запустить через команду python3 manage.py runserver


### Создание суперпользователя 

- Введите в консоль команду python manage.py createsuperuser

## Используемые технологии:

1. Django REST Framework
2. Simple_jwt для токенов
3. DRF 
4. PostgreSQL
5. Python 
6. Swagger

## Права доступа:

- Анонимный пользователь не видит никаких товаров
  - Пользователь может:
    - Получать список объявлений
    - Создавать объявление
    - Редактировать и удалять своё объявление
  - Администратор может:
    - Дополнительно к правам пользователя редактировать или удалять объявления к объявлениям любых других пользователей, так же имеет доступ к изменению или удалению любого пользователя
