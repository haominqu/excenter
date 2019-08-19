from django.db import models

# Create your models here.
ROLE_CHOICES = (
    (0, '超级管理员'),
    (1, '管理员'),
    (2, '员工'),
    (3, '来宾'),
    (4, '游客'),
)

ACTIVE_CHOICES = (
    (0, '未激活'),
    (1, '激活'),
    (2, '锁定'),
)

AUDIT_CHOICES = (
    (0,'未审核'),
    (1,'审核通过'),
    (2,'未通过'),
)

class UserInfo(models.Model):
    username = models.CharField(verbose_name="登录名", max_length=30,null=False)
    password = models.CharField(verbose_name='密码', max_length=200,null=False)
    role = models.IntegerField(verbose_name='用户角色', choices=ROLE_CHOICES, default=4)
    is_active = models.IntegerField(verbose_name='激活状态', choices=ACTIVE_CHOICES, default=0)

    def __str__(self):
        return self.username

class Guest(models.Model):
    user = models.OneToOneField(UserInfo, verbose_name="用户")
    invite = models.ForeignKey(UserInfo, verbose_name='邀请人', related_name='inviter')
    realname = models.CharField(verbose_name="用户名", max_length=30, null=False)
    audit_status = models.IntegerField(verbose_name='审核状态', choices=AUDIT_CHOICES, default=0)
    face_picture = models.ImageField(verbose_name='面部照片', upload_to='image/guest/face', default='normal.png')

    def __str__(self):
        return self