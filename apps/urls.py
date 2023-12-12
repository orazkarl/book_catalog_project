from django.urls import include, path

urlpatterns = [
    path('', include('apps.book_catalog.api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
