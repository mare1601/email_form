from django.conf.urls import patterns, url

from . import views

urlpatterns = [
  url(r'^$', views.main_page, name='main_page'),
  url(r'^create_post/$', views.main_page, name='create_post'),
]