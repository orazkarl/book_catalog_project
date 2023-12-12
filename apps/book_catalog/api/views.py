from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.book_catalog.api.serializers import (AuthorSerializer,
                                               BookSerializer,
                                               FavoriteBookSerializer,
                                               GenreSerializer,
                                               ReviewSerializer)
from apps.book_catalog.models import Author, Book, FavoriteBook, Genre, Review


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genre', 'author', 'publication_date']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'user', 'rating']


class FavoriteBookViewSet(viewsets.ModelViewSet):
    queryset = FavoriteBook.objects.all()
    serializer_class = FavoriteBookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'user']
