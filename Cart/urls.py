from django.conf.urls import url

from Cart import views

urlpatterns=[
    url(r'^cart/',views.cart,name='cart'),

#     添加到购物车
    url(r'^addToCart/',views.addToCart),

#     减少购物车商品数量
    url(r'^subToCart/',views.subToCart),

#     改变购物车选中状态
    url(r'^changeStatus/',views.changeStatus),

#     全选
    url(r'^allSelect/',views.allSelect),
]