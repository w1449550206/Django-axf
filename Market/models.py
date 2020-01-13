from django.db import models

# Create your models here.


# insert into axf_foodtype
# (typeid,typename,childtypenames,typesort) values
# ("104749","热销榜","全部分类:0",1)


class AxfFoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=64)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtype'


# goods
# axf_goods (id, productid, productimg, productname, productlongname,
#           isxf, pmdesc, specifics, price, marketprice,
#            categoryid, childcid, childcidname, dealerid, storenums, productnum)
# VALUES (1, 11951, '/media/images/goods016.jpg', '', '乐吧薯片鲜虾味50.0g',
#       0, 0, '50g', 2, 2.5,
#     103541, 103543, '膨化食品', 4858, 200, 4);


class AxfGoods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=128)
    productname = models.CharField(max_length=64)
    productlongname = models.CharField(max_length=128)

    isxf = models.BooleanField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=16)
    price = models.FloatField()
    marketprice = models.FloatField()

    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=64)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'
