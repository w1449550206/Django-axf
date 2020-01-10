from django.conf.urls import url

from Market import views

urlpatterns = [
    url(r'^market/',views.market,name='market'),
]