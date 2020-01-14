from django.conf.urls import url

from Cart import views

urlpatterns=[
    url(r'^cart/',views.cart,name='cart'),

#     添加到购物车
    url(r'^addToCart/',views.addToCart),
]