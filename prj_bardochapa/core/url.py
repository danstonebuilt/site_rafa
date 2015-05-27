__author__ = 'daniel.anselmo'

from django.conf.urls import url

urlpatterns = [
    url(r'^home/', 'core.views.homepage'),
    url(r'^path/', 'core.views.show_path')
]
