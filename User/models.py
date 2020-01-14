from django.db import models

# Create your models here.


class AxfUser(models.Model):

    # 用户名
    name = models.CharField(max_length=32)
    # 密码
    password = models.CharField(max_length=256)
    # 邮箱
    email = models.EmailField()
    # 头像
    icon = models.ImageField(upload_to='icons')
    # 激活状态
    active = models.BooleanField(default=False)

    # 唯一标识
    token = models.CharField(max_length=256)


    class Meta:
        db_table = 'axfuser'
