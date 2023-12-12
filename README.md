# Каталог книг

## Требования

1. Python 3.x
2. Django
3. Django REST Framework
4. Django-filter (для фильтрации в API)
5. djoser (для регистрации и аутентификации)

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Настройка проекта

### Создайте и примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Создайте суперпользователя:
```bash
python manage.py createsuperuser
```

### Запустите сервер разработки:
```bash
python manage.py runserver
```
## Использование API

API предоставляет следующие эндпоинты:

- `/api/books/` (жанр книги)
- `/api/books/` - Список всех книг и их детали.
- `/api/authors/` - Список всех авторов и их детали.
- `/api/genres/` - Список всех жанров и их детали.
- `/api/reviews/` - Список отзывов и их детали.
- `/api/favorites/` - Список избранных книг и их детали.

## Админ панель
`/api/admin`


## Swagger
`/api/schema/swagger-ui/`