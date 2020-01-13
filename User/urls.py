from django.conf.urls import url

from User import views

urlpatterns = [
    url(r'^login',views.login),
    url(r'^register',views.register,name='register'),

#     用户名字的后台验证
    url(r'^checkName/',views.checkName),
]