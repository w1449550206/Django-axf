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
