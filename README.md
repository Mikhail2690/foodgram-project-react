# Проект Foodgram – Продуктовый помощник

## Описание проекта.

На этом сервисе пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## Стек технологий.

- Python 3.9
- Django 3.2
- djangorestframework 3.14
- Gunicorn
- Nginx
- PostgreSQL
- Docker


## Как запустить проект локально, используя Docker:
- Установить Docker и docker-compose
- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Mikhail2690/foodgram-project-react.git
```
```
cd foodgram-project-react/
```

- В корневой папке проекта создайте файл .env, в котором заполните следующие переменные окружения:
```
touch .env
```

```
SECRET_KEY=<Your_secret_key>
DEBUG=False
ALLOWED_HOSTS=<Your_allowed_host>
POSTGRES_USER=django_user
POSTGRES_PASSWORD=<Your_password>
POSTGRES_DB=django
DB_HOST=db
DB_PORT=5432
```

- Запустите docker-compose в корневой директории командой:

```
docker compose up -d --build
```

- Выполните миграции, соберите статику и копируйте её в необходимую дерикторию:

```
docker compose exec backend python manage.py migrate

docker compose exec backend python manage.py collectstatic --no-input

docker compose exec backend cp -r /app/collected_static/. /app/static/
```
- Создайте суперюзера и загрузите предустановленый список ингредиентов
```
docker compose exec backend python manage.py createsuperuser

docker compose exec backend python manage.py load_data
```
- Проверить работу
```
http://localhost:8000/
```
- Документация
```
http://localhost:8000/api/docs/
```
## В API доступны следующие эндпоинты:
- /api/users/ Get-запрос – получение списка пользователей. POST-запрос – регистрация нового пользователя. Доступно без токена.

- /api/users/{id} GET-запрос – персональная страница пользователя с указанным id (доступно без токена).

- /api/users/me/ GET-запрос – страница текущего пользователя. PATCH-запрос – редактирование собственной страницы. Доступно авторизированным пользователям.

- /api/users/set_password POST-запрос – изменение собственного пароля. Доступно авторизированным пользователям.

- /api/auth/token/login/ POST-запрос – получение токена. Используется для авторизации по емейлу и паролю, чтобы далее использовать токен при запросах.

- /api/auth/token/logout/ POST-запрос – удаление токена.

- /api/tags/ GET-запрос — получение списка всех тегов. Доступно без токена.

- /api/tags/{id} GET-запрос — получение информации о теге о его id. Доступно без токена.

- /api/ingredients/ GET-запрос – получение списка всех ингредиентов. Доступно без токена.

- /api/ingredients/{id}/ GET-запрос — получение информации об ингредиенте по его id. Доступно без токена.

- /api/recipes/ GET-запрос – получение списка всех рецептов. Возможен поиск рецептов по тегам (доступно без токена). POST-запрос – добавление нового рецепта (доступно для авторизированных пользователей).

- /api/recipes/{id}/ GET-запрос – получение информации о рецепте по его id (доступно без токена). PATCH-запрос – изменение собственного рецепта (доступно для автора рецепта). DELETE-запрос – удаление собственного рецепта (доступно для автора рецепта).

- /api/recipes/{id}/favorite/ POST-запрос – добавление нового рецепта в избранное. DELETE-запрос – удаление рецепта из избранного. Доступно для авторизированных пользователей.

- /api/recipes/{id}/shopping_cart/ POST-запрос – добавление нового рецепта в список покупок. DELETE-запрос – удаление рецепта из списка покупок. Доступно для авторизированных пользователей.

- /api/recipes/download_shopping_cart/ GET-запрос – получение текстового файла со списком покупок. Доступно для авторизированных пользователей.

- /api/users/{id}/subscribe/ POST-запрос – подписка на пользователя с указанным id. DELETE-запрос – отписка от пользователя с указанным id. Доступно для авторизированных пользователей

- /api/users/subscriptions/ GET-запрос – получение списка всех пользователей, на которых подписан текущий пользователь Доступно для авторизированных пользователей.

Автор: [Федоренко Михаил](https://github.com/Mikhail2690/)
