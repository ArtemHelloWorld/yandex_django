<h1 align="center">Django intensiv by <a href="https://t.me/@artemstreeter" target="_blank">Artem</a> </h1>

[![Python package](https://github.com/ArtemVX/yandex_django/actions/workflows/python-package.yml/badge.svg)](https://github.com/ArtemVX/yandex_django/actions/workflows/python-package.yml)



<h2>Установка зависимостей</h2>

<h3>Основные</h3>
pip install -r requirements.txt

<h3>Дополнительные </h3>
1. Для тестов pip install -r requirements-test.txt
2. Для разработки pip install -r requirements-development.txt



<h2>Чтобы запустить проект в dev-режиме</h2>
1. Установите основные зависимости 
2. Добавьте в корневой каталог файл .env, содержащий поля SECRET_KEY и DEBUG. Пример можно посмотреть в файле .env-example
4. Запустите локальный сервер python app/manage.py runserver
