from django.conf.urls import url, patterns
from courses import views

urlpatterns = patterns('', url(r'^$', views.course_list, name='course_list'),
                       url(r'^(?P<course_name_slug>[\w\-]+)/$', views.course, name='courses'),)