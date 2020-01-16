from django.conf.urls import url

from Order import views

urlpatterns=[
    url(r'^makeOrder/',views.makeOrder),
    url(r'^orderDetail/',views.orderDetail)
]