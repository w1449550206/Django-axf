from django.db import models

# Create your models here.
from Market.models import AxfGoods
from User.models import AxfUser


class AxfCart(models.Model):
    c_user = models.ForeignKey(AxfUser)

    c_goods = models.ForeignKey(AxfGoods)

    c_is_select = models.BooleanField(default=True)

    c_goods_num = models.IntegerField(default=1)


    class Meta:
        db_table = 'axf_cart'
