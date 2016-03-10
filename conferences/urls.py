from django.conf.urls import url, patterns
from conferences import views

urlpatterns = patterns('', url(r'^$', views.conference_list, name='conference_list'),
                       url(r'^(?P<conference_name_slug>[\w\-]+)/$', views.conference, name='conferences'),)