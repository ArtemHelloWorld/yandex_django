<h1 align="center">Django intensiv by <a href="https://t.me/@artemstreeter" target="_blank">Artem</a> </h1>

[![Python package](https://github.com/ArtemVX/yandex_django/actions/workflows/python-package.yml/badge.svg)](https://github.com/ArtemVX/yandex_django/actions/workflows/python-package.yml)
[![django | tests](https://github.com/ArtemVX/yandex_django/actions/workflows/django-tests.yml/badge.svg)](https://github.com/ArtemVX/yandex_django/actions/workflows/django-tests.yml)


<h2>Чтобы запустить проект в dev-режиме</h2>
<p>1. Установите основные зависимости </p>
<p>2. Добавьте в корневой каталог файл .env, содержащий поля SECRET_KEY; DEBUG; REVERSE_MIDDLEWARE; ALLOWED_HOSTS.<br><h5>Пример можно посмотреть в файле .env-example</h5>Используйте надежный ключ, содержащий больше 50 символов.<br>Для поля Debug установите True, если проект находится на стадии разработки и вам необходимо видеть детальную информацию об ошибках, и установите development зависимости(requirements/requirements-development.txt).<br>Для рабочего сервера необходимо указать DEBUG=False и перечислить доступные хосты в поле ALLOWED_HOSTS. Используйте запятую(без пробелов) для указания нескольких достпных хостов. Установите REVERSE_MIDDLEWARE значение Active, чтобы включить middleware, отвечающий за переворачивание русских слов в каждом 10 запросе(Параметр REVERSE_MIDDLEWARE не влияет на наличие данного middleware в settings, а меняет его работу). <br></p>
<p>3. Запустите локальный сервер <pre><code>python app/manage.py runserver</code></pre></p>


<h2>Установка зависимостей</h2>


<h4>Основные | Django & dotenv</h4>
<pre><code>pip install -r requirements-prod.txt</code></pre>

<h4>Дополнительные </h4>
<p>Для тестов | pytest<pre><code>pip install -r requirements-test.txt</code></pre></p>
<p>Для разработки | black & flake8 <pre><code>pip install -r requirements-development.txt</code></pre></p>
