from django.conf.urls import url

from User import views

urlpatterns = [
    url(r'^login',views.login,name='login'),
    url(r'^register',views.register,name='register'),

#     用户名字的后台验证
    url(r'^checkName/',views.checkName),

#     发送邮件
    url(r'^testSendMail/',views.testSendMail),

#     激活帐号
    url(r'^account/',views.account),

#     验证码
    url(r'^get_code/',views.get_code),

#     退出
    url(r'^logout/',views.logout,name='logout')
]