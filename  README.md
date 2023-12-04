<h3 align="center">
Программа отчета получения документов.</h3>

Микросервис позволяет отправлять письмо о загрузке документа на сервис и
Принимать или отклонять данный докуент администратором.

Стек проекта: <br>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 -3.10
<br>
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
<br>![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
Сопутствующие пакеты можно посмотреть в pyproject.toml

Документация redoc, swagger доступна после запуска проекта
БД - ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) 
<br>данные вынесены в .env

**Перед запуском** создать и заполнить СВОЙ файл .env СВОИМИ данными

#### ___Состав файла env.___

DB_ENGINE=django.db.backends.postgresql
<br>DB_NAME=
<br>DB_USER=
<br>DB_PASSWORD=
<br>DB_HOST=127.0.0.1
<br>DB_PORT=5432 (db - для докера)

_Данные отправки писем_

EMAIL_HOST = 
EMAIL_PORT = 
EMAIL_HOST_USER = 
EMAIL_HOST_PASSWORD = 
EMAIL_USE_SSL = True

#### _Запуск в докер контейнере_
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

docker-compose build

docker-compose up

#### Тесты
Покрытие 89% unitest
Запуск тестов - coverage run --source='.' manage.py test
Посмотреть покрытие - coverage report

Проект выполнил Галиулин Ярослав на IDE
<br>![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)
