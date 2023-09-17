![Megano.png](..%2FDoc%2FMegano.png)
# Интернет-магазин на базе Django и Vue3
Основные технологии
----------------
* Frontend: HTML5, CSS3, JS, Vue3
* Backend: python 3.10, django 4.2, django rest framework 3.14
* Работа с данными реализована в СУБД SQLite

Особенности
----------------

* Frontend и backend обмениваются посредством API написанном на DRF

Инструкция по установке и первому запуску 
-----------------------------------------
### Установка обычным способом:

1. Скопировать файлы проекта в локальную директорию
2. Установить Frontend
```commandline
pip install diploma-frontend-0.6.tar.gz
```
3. Установить зависимости из requirements.txt:
```commandline
pip install -r requirements.txt
```
*Рекомендуется настроить [виртуальное окружение](https://docs.python.org/3/library/venv.html).*
4. Выполнить настройку баз данных
```commandline
python manage.py makemigrations
python manage.py migrate
```
5. Создать пользователя-администратора
```commandline
python manage.py createsuperuser
```

6. Запустить приложение
```commandline
python manage.py runserver 
```

Работа с интернет-магазином
------------------------
### Начало работы
Для начала работы откройте в web-браузере страницу [127.0.0.1:8000](http://127.0.0.1:8000/):

### Конфигурация магазина
Для начального конфигурирования откройте [панель администрирования](http://127.0.0.1:8000/admin): 


