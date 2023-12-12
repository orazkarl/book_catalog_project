from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.book_catalog.api.views import (AuthorViewSet, BookViewSet,
                                         FavoriteBookViewSet, GenreViewSet,
                                         ReviewViewSet)

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'favorites', FavoriteBookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
