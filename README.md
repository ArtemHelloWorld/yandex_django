# yandex_django
![This is an image](https://github.com/ArtemVX/yandex_django/actions/workflows/python-package.yml/badge.svg)

Установка зависимостей

Основные pip install -r requirements.txt

Дополнительные 
1. Для тестов pip install -r requirements-test.txt
2. Для разработки pip install -r requirements-development.txt


Чтобы запустить проект в dev-режиме
1. Установите основные зависимости 
2. Добавьте в корневой каталог файл .env, содержащий поля SECRET_KEY и DEBUG. Пример можно посмотреть в файле .env-example
4. Запустите локальный сервер python app/manage.py runserver
