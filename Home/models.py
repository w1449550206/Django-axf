from django.db import models

# Create your models here.

#轮播
# 从数据库中读取图片的路径 然后将路径渲染到页面的img的src中

# 观察别人网站的数据类型
# INSERT INTO axf wheel (id, img, name, trackid)
# （1, '/media/images/ad02.jpg','酸奶女王',21870）

class AxfWheel(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_wheel'

# 导航nav


# INSERT INTO axf_nav (id, img, name, trackid) VALUES (1, '/media/images/banner16.jpg', '每日必抢', 21851);
# INSERT INTO axf_nav (id, img, name, trackid) VALUES (2, '/media/images/banner12.jpg', '每日签到', 21753);
# INSERT INTO axf_nav (id, img, name, trackid) VALUES (3, '/media/images/banner13.jpg', '鲜货直供', 21749);
# INSERT INTO axf_nav (id, img, name, trackid) VALUES (4, '/media/images/banner14.jpg', '鲜蜂力荐', 21854);

class AxfNav(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_nav'


#mustbuy


# INSERT INTO axf_mustbuy (id, img, name, trackid) VALUES (1, '/media/images/ad01.jpg', '酸奶女王', 21870);
# INSERT INTO axf_mustbuy (id, img, name, trackid) VALUES (2, '/media/images/ad02.jpg', '鲜果女王', 21861);
# INSERT INTO axf_mustbuy (id, img, name, trackid) VALUES (3, '/media/images/ad01.jpg', '麻辣女王', 21866);
# INSERT INTO axf_mustbuy (id, img, name, trackid) VALUES (4, '/media/images/ad02.jpg', '鲜货直供－果析', 21858);

class AxfMustBuy(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_mustbuy'


# mainshow

# INSERT INTO axf_mainshow
# (id, img, name, trackid, categoryid, brandname,
# img1, childcid1, productid1, longname1, price1, marketprice1,
# img2, childcid2, productid2, longname2, price2, marketprice2,
# img3, childcid3, productid3, longname3, price3, marketprice3)
# VALUES (1, '/media/images/ad01.jpg', '优选水果', 21782, 103532, '爱鲜蜂', '/media/images/goods002.jpg', 103533, 118824, '爱鲜蜂·特小凤西瓜1.5-2.5kg/粒', 25.8, 25.8, '/media/images/goods003.jpg', 103534, 116950, '蜂觅·越南直采红心火龙果350-450g/盒', 15.3, 15.8, '/media/images/goods010.jpg', 103533, 118826, '爱鲜蜂·海南千禧果400-450g/盒', 9.9, 13.8);

class AxfMainShow(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=128)

    img1=models.CharField(max_length=128)
    childcid1= models.IntegerField()
    productid1= models.IntegerField()
    longname1=models.CharField(max_length=128)
    price1=models.FloatField()
    marketprice1=models.FloatField()

    img2=models.CharField(max_length=128)
    childcid2= models.IntegerField()
    productid2= models.IntegerField()
    longname2=models.CharField(max_length=128)
    price2=models.FloatField()
    marketprice2=models.FloatField()

    img3=models.CharField(max_length=128)
    childcid3= models.IntegerField()
    productid3= models.IntegerField()
    longname3=models.CharField(max_length=128)
    price3=models.FloatField()
    marketprice3=models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'

# INSERT INTO axf_mainshow (id, img, name, trackid, categoryid, brandname, img1, childcid1, productid1, longname1, price1, marketprice1, img2, childcid2, productid2, longname2, price2, marketprice2, img3, childcid3, productid3, longname3, price3, marketprice3) VALUES (1, '/media/images/ad01.jpg', '优选水果', 21782, 103532, '爱鲜蜂', '/media/images/goods002.jpg', 103533, 118824, '爱鲜蜂·特小凤西瓜1.5-2.5kg/粒', 25.8, 25.8, '/media/images/goods003.jpg', 103534, 116950, '蜂觅·越南直采红心火龙果350-450g/盒', 15.3, 15.8, '/media/images/goods010.jpg', 103533, 118826, '爱鲜蜂·海南千禧果400-450g/盒', 9.9, 13.8);
# INSERT INTO axf_mainshow (id, img, name, trackid, categoryid, brandname, img1, childcid1, productid1, longname1, price1, marketprice1, img2, childcid2, productid2, longname2, price2, marketprice2, img3, childcid3, productid3, longname3, price3, marketprice3) VALUES (2, '/media/images/ad02.jpg', '牛奶面包', 21782, 103532, '爱鲜蜂', '/media/images/goods002.jpg', 103533, 118824, '爱鲜蜂·特小凤西瓜1.5-2.5kg/粒', 25.8, 25.8, '/media/images/goods003.jpg', 103534, 116950, '蜂觅·越南直采红心火龙果350-450g/盒', 15.3, 15.8, '/media/images/goods010.jpg', 103533, 118826, '爱鲜蜂·海南千禧果400-450g/盒', 9.9, 13.8);
# INSERT INTO axf_mainshow (id, img, name, trackid, categoryid, brandname, img1, childcid1, productid1, longname1, price1, marketprice1, img2, childcid2, productid2, longname2, price2, marketprice2, img3, childcid3, productid3, longname3, price3, marketprice3) VALUES (3, '/media/images/ad01.jpg', '卤味熟食', 21782, 103532, '爱鲜蜂', '/media/images/goods002.jpg', 103533, 118824, '爱鲜蜂·特小凤西瓜1.5-2.5kg/粒', 25.8, 25.8, '/media/images/goods003.jpg', 103534, 116950, '蜂觅·越南直采红心火龙果350-450g/盒', 15.3, 15.8, '/media/images/goods010.jpg', 103533, 118826, '爱鲜蜂·海南千禧果400-450g/盒', 9.9, 13.8);
# INSERT INTO axf_mainshow (id, img, name, trackid, categoryid, brandname, img1, childcid1, productid1, longname1, price1, marketprice1, img2, childcid2, productid2, longname2, price2, marketprice2, img3, childcid3, productid3, longname3, price3, marketprice3) VALUES (4, '/media/images/ad02.jpg', '饮料酒水', 21782, 103532, '爱鲜蜂', '/media/images/goods002.jpg', 103533, 118824, '爱鲜蜂·特小凤西瓜1.5-2.5kg/粒', 25.8, 25.8, '/media/images/goods003.jpg', 103534, 116950, '蜂觅·越南直采红心火龙果350-450g/盒', 15.3, 15.8, '/media/images/goods010.jpg', 103533, 118826, '爱鲜蜂·海南千禧果400-450g/盒', 9.9, 13.8);
# INSERT INTO axf_mainshow (id, img, name, trackid, categoryid, brandname, img1, childcid1, productid1, longname1, price1, marketprice1, img2, childcid2, productid2, longname2, price2, marketprice2, img3, childcid3, productid3, longname3, price3, marketprice3) VALUES (5, '/media/images/ad01.jpg', '零食大趴', 21782, 103532, '爱鲜蜂', '/media/images/goods002.jpg', 103533, 118824, '爱鲜蜂·特小凤西瓜1.5-2.5kg/粒', 25.8, 25.8, '/media/images/goods003.jpg', 103534, 116950, '蜂觅·越南直采红心火龙果350-450g/盒', 15.3, 15.8, '/media/images/goods010.jpg', 103533, 118826, '爱鲜蜂·海南千禧果400-450g/盒', 9.9, 13.8);
# INSERT INTO axf_mainshow (id, img, name, trackid, categoryid, brandname, img1, childcid1, productid1, longname1, price1, marketprice1, img2, childcid2, productid2, longname2, price2, marketprice2, img3, childcid3, productid3, longname3, price3, marketprice3) VALUES (6, '/media/images/ad02.jpg', '方便速食', 21782, 103532, '爱鲜蜂', '/media/images/goods002.jpg', 103533, 118824, '爱鲜蜂·特小凤西瓜1.5-2.5kg/粒', 25.8, 25.8, '/media/images/goods003.jpg', 103534, 116950, '蜂觅·越南直采红心火龙果350-450g/盒', 15.3, 15.8, '/media/images/goods010.jpg', 103533, 118826, '爱鲜蜂·海南千禧果400-450g/盒', 9.9, 13.8);
