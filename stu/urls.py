#coding=utf-8
from django.conf.urls import url
from stu import views

urlpatterns = [
    # url(r'^login/',views.IndexView.as_view()),
    # url(r'^register/',views.RegisterView.as_view()),
    url(r'^only/',views.onlyView),
    url(r'^only/',views.existView),
]