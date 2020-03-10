from django.db import models

# Create your models here.
from Market.models import AxfGoods
from User.models import AxfUser


class AxfOrder(models.Model):
    o_user = models.ForeignKey(AxfUser)
    o_price = models.FloatField()

    class Meta:
        db_table = 'axf_order'

class AxfOrderGoods(models.Model):
    og_order = models.ForeignKey(AxfOrder)
    og_goods = models.ForeignKey(AxfGoods)

    og_num = models.IntegerField()

    class Meta:
        db_table = 'axf_ordergoods'