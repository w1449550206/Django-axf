from django.conf.urls import url

from Cart import views

urlpatterns = [
    url(r'^cart/',views.cart,name='cart')
]