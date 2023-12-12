from django.contrib import admin

from apps.book_catalog.models import Author, Book, FavoriteBook, Genre, Review


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'author', 'publication_date')
    list_filter = ('genre', 'author', 'publication_date')
    search_fields = ('title', 'author__name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating', 'text')
    list_filter = ('book', 'user', 'rating')
    search_fields = ('book__title', 'user__username')


@admin.register(FavoriteBook)
class FavoriteBookAdmin(admin.ModelAdmin):
    list_display = ('book', 'user')
    list_filter = ('book', 'user')
    search_fields = ('book__title', 'user__username')
