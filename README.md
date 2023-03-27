<h1 align="center">Django intensiv by <a href="https://t.me/@artemstreeter" target="_blank">Artem</a> </h1>

[![Python package](https://github.com/ArtemVX/yandex_django/actions/workflows/python-package.yml/badge.svg)](https://github.com/ArtemVX/yandex_django/actions/workflows/python-package.yml)
[![django | tests](https://github.com/ArtemVX/yandex_django/actions/workflows/django-tests.yml/badge.svg)](https://github.com/ArtemVX/yandex_django/actions/workflows/django-tests.yml)


<h2>Чтобы запустить проект в dev-режиме</h2>

1. Установите основные зависимости(смотреть ниже)  <br>

2. Добавьте в корневой каталог файл .env(Пример можно посмотреть в файле .env-example), содержащий поля:

* SECRET_KEY Используйте надежный ключ, содержащий больше 50 символов

* DEBUG Установите True, если проект находится на стадии разработки и вам необходимо видеть детальную информацию об ошибках, и установите Debug development зависимости(requirements/requirements-development.txt) Для рабочего сервера необходимо указать DEBUG=False и перечислить доступные хосты в поле ALLOWED_HOSTS

* ALLOWED_HOSTS Используйте запятую(без пробелов) для указания нескольких доступных хостов

* DJANGO_SUPERUSER_USERNAME; DJANGO_SUPERUSER_EMAIL; DJANGO_SUPERUSER_PASSWORD Укажите, чтобы создать супер юзера командной  initdata  (ниже описание команды)

* EMAIL_TO_SEND_MESSAGES Стандартная почта для отправки сообщений

* KEY32 Используется для шифрования ссылкой для активации аккаунта

* ACTIVATE_USERS Установите True, если хотите, чтобы после регистрации все пользователи были автоматически активны

* MAX_FAILED_LOGIN_ATTEMPTS Максимальное число попыток входа в аккаунт

* REVERSE_MIDDLEWARE Установите значение Active, чтобы включить middleware, отвечающий за переворачивание русских слов в каждом 10 запросе(Параметр REVERSE_MIDDLEWARE не влияет на наличие данного middleware в settings, а меняет его работу)

* RATE_LIMIT_MIDDLEWARE Установите True, чтобы ограничить количество запросов с одного IP

* REQUESTS_PER_SECOND Максимальное количество запросов в секунду. Понадобится, если включен RATE_LIMIT_MIDDLEWARE


3. Запустите локальный сервер <pre><code>python lyceum/manage.py runserver</code></pre>


<h2>Установка зависимостей</h2>


<h4>Основные | Django & dotenv</h4>
<pre><code>pip install -r requirements-prod.txt</code></pre>

<h4>Дополнительные </h4>
Для тестов | pytest & freezegun <pre><code>pip install -r requirements-test.txt</code></pre>
Для разработки | black & flake8 & isort & toolbar <pre><code>pip install -r requirements-dev.txt</code></pre>

<h2>Создание базы данных</h2>
Чтобы создать бд, первым шагом необходимо выполнить миграции. С этим вам поможет команда<pre><code>python lyceum/manage.py migrate</code></pre>Дождитесь выполнения миграций
Наглядную структуры бд, в виде er-диаграммы вы можете посмотреть в папке ./er_models <br>
После того, как вы создали пустую бузу данных вы можете внести в нее тестовые данные. Такие данные вы можете найти в пакетах приложений в папках fixtures. Пример с загрузкой данных из приложения catalog: <pre><code>python lyceum/manage.py loaddata lyceum/catalog/fixtures/data.json</code></pre>

<h2>Инициализация данных</h2>
После установки необходимых зависимостей вы можете воспользоваться кастомной командой initdata<pre><code>python lyceum/manage.py initdata</code></pre>Эта команды выполнит следующие шаги:

1. Проверит базу данных на все миграции. --skip-checking-database для отключения

2. Загрузит необходимые данные из фикстур. --skip-loading-data для отключения

3. Создат администратора --skip-creating-superuser для отключения. Чтобы внести свои данные для администратора:

* Укажите в виртуальном окружении(.env) следующие поля: DJANGO_SUPERUSER_USERNAME; DJANGO_SUPERUSER_EMAIL; DJANGO_SUPERUSER_PASSWORD

* Добавьте в команду аргумент --interactive, чтобы ввести данные вручную. Кроме того, вы можете ввести не указывать этот аргумент и не добавить какие-то поля в виртуально окружение, а ввести их вручную