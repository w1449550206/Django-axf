from django.conf.urls import url

from Home import views

urlpatterns=[
    url(r'^home/',views.home,name='home'),
]