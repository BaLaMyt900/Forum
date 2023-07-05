### Итоговый проект - Форумник
![hippo](https://i.imgur.com/6AqWIPA.gif)
 В проекте использованы:
- Django
- django-allauth 
- celery[redis]
- redis 
- python-dotenv 
- django-summernote

Новостная рассылка.<br>
Добавлена функция новостной рассылки.<br>
По умолчанию отправляет всем пользователям список последних новостей за прошлую неделю в понедельник в 8 утра.<br>
Включить можно через settings

Модели:
- Announce - Модель объявления
- Category - Модель категории объявления
- Responce - Модель отклика на объявление
- Notification - Модель уведомления о новых откликах

ENV Файл:
Содержит конфигурацию для почты.
Название `email_config.env`
- PASSWORD=***** - Пароль от аккаунта почты для рассылки
- LOGIN=****** - Логин от почты для рассылки. (Только логин без указания хоста)

Объявления:
- Используется WYSIWYG редактор summernote
- Редактирование доступно со страницы просмотра статьи, если зашел её автор.

Профиль:
- Реализовано управление профилем с помощью окна справа
- Список объявлений и уведомления о наличии новых откликов

Живой чат:
 - Реализовано отдельное окно с живым чатом.
 - Есть дополнительная модель с сообщением чата
 - При неавторизированном пользователе, использует предсозданный пользователь "Аноним"

AJAX:
- Реализована авторизация через окно профиля
- Реализована отправка сообщения в живой чат, загрузка последних сообщений, потоковая загрузка недавних сообщений


#### Запуск
Настроен автоматический запуск всего проекта через docker-compose.<br>
Для перейдите в каталог проекта и введите команду:
`docker-compose up --build`
##### ВАЖНО! docker-engine должен быть запущен!
