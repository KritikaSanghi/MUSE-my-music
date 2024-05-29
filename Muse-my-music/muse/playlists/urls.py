from django.contrib import admin
from django.urls import include, path
from playlists import views
urlpatterns = [
        path('', views.home, name='home'),
        path('Artists', views.Artists, name='Artists'),
        path('Albums', views.Albums, name='Albums')
    ]
