from django.conf.urls import url

from HomeApp import views

urlpatterns = [
    url(r'^home/',views.home)
]