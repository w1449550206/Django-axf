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
