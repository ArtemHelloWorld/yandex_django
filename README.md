<h1 align="center">Django intensiv by <a href="https://t.me/@artemstreeter" target="_blank">Artem</a> </h1>

[![Python package](https://github.com/ArtemVX/yandex_django/actions/workflows/python-package.yml/badge.svg)](https://github.com/ArtemVX/yandex_django/actions/workflows/python-package.yml)
[![django | tests](https://github.com/ArtemVX/yandex_django/actions/workflows/django-tests.yml/badge.svg)](https://github.com/ArtemVX/yandex_django/actions/workflows/django-tests.yml)


<h2>Чтобы запустить проект в dev-режиме</h2>
1. Установите основные зависимости  <br>
2. Добавьте в корневой каталог файл .env(Пример можно посмотреть в файле .env-example), содержащий поля:<br>
SECRET_KEY Используйте надежный ключ, содержащий больше 50 символов<br>
DEBUG Установите True, если проект находится на стадии разработки и вам необходимо видеть детальную информацию об ошибках, и установите Debug development зависимости(requirements/requirements-development.txt) Для рабочего сервера необходимо указать DEBUG=False и перечислить доступные хосты в поле ALLOWED_HOSTS<br>
REVERSE_MIDDLEWARE<br>
ALLOWED_HOSTS Используйте запятую(без пробелов) для указания нескольких достпных хостов<br>
REVERSE_MIDDLEWARE Установите REVERSE_MIDDLEWARE значение Active, чтобы включить middleware, отвечающий за переворачивание русских слов в каждом 10 запросе(Параметр REVERSE_MIDDLEWARE не влияет на наличие данного middleware в settings, а меняет его работу)<br>

3. Запустите локальный сервер <pre><code>python lyceum/manage.py runserver</code></pre>


<h2>Установка зависимостей</h2>


<h4>Основные | Django & dotenv</h4>
<pre><code>pip install -r requirements-prod.txt</code></pre>

<h4>Дополнительные </h4>
Для тестов | pytest<pre><code>pip install -r requirements-test.txt</code></pre>
Для разработки | black & flake8 <pre><code>pip install -r requirements-development.txt</code></pre>

<h2>Создание базы данных</h2>
Чтобы создать бд, первым шагом необходимо выполнить миграции. С этим вам поможет команда<pre><code>python lyceum/manage.py migrate</code></pre>Дождитесь выполнения миграций
Наглядную структуры бд, в виде er-диаграммы вы можете посмотреть в папке ./er_models <br>
После того, как вы создали пустую бузу данных вы можете внести в нее тестовые данные. Такие данные вы можете найти в пакетах приложений в папках fixtures. Пример с загрузкой данных из приложения catalog: <pre><code>python lyceum/manage.py loaddata lyceum/catalog/fixtures/data.json</code></pre>

<h2>Инициализация данных</h2>
После установки необходимых зависимостей вы можете воспользоваться кастомной командой initdata<pre><code>python lyceum/manage.py initdata</code></pre>Эта команды выполнит следующие шаги:
1. Проверит базу данных на все миграции. --skip-checking-database для отключения
2. Загрузит необходимые данные из фикстур. --skip-loading-data для отключения
3. Создат администратора. Чтобы внести свои данные для администратора:
<h6>Укажите в виртуальном окружении(.env) слудющие поля: DJANGO_SUPERUSER_USERNAME; DJANGO_SUPERUSER_EMAIL; DJANGO_SUPERUSER_PASSWORD </h6>
<h6>Добавьте в команду аргумент --interactive чтобы ввести данные вручную. Кроме того, вы можете ввести не казывать этот аршумент и не добовить какие-то поля в виртуально окружение, а ввести их вручную</h6>