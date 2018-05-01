from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^students/$', views.student_list, name='student-list'),
    url(r'^students/(?P<pk>[0-9]+)/$', views.student_detail, name='student-detail'),
    url(r'^me/(?P<pk>[0-9]+)/$', views.student_detail, name='me-detail'),
    url(r'^me/(?P<pk>[0-9]+)/$', views.student_detail, name='student-list'),
]