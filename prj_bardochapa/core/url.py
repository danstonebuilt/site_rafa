__author__ = 'daniel.anselmo'


from django.conf.urls import include, url
from django.contrib import admin
from core.views import show_path


urlpatterns = [
    url(r'^home/',show_path),
]

