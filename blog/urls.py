
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import index, post, about, projects


urlpatterns = [
    path('', index, name='index'),
    path('post/', post, name='post'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects')
]