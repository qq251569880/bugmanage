from django.conf.urls import patterns, url
from debug import views
urlpatterns = patterns('',
      url(r'^$', views.index, name='index'),
      )
