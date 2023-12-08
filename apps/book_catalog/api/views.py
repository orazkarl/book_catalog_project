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


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class FavoriteBookViewSet(viewsets.ModelViewSet):
    queryset = FavoriteBook.objects.all()
    serializer_class = FavoriteBookSerializer
