from django.conf.urls import patterns, url

from emailform import views

urlpatterns = [
  url(r'^$', views.main_page, name='main_page'),
  #url(r'^create_post/$', views.main_page, name='create_post'),

  # views.create_post is the POST
  url(r'^create_post/$', views.create_post, name='create_post')
]
