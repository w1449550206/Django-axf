from django.conf.urls import url

from Mine import views

urlpatterns = [
    url(r'^mine/',views.mine,name='mine')
]