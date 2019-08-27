from django.db import models
from django.utils import timezone
from userinfo.models import UserInfo
from machine.models import Machine

# Create your models here.
class UseHistory(models.Model):
    userid = models.CharField(verbose_name="用户id", max_length=50, default='')
    macid = models.CharField(verbose_name="感应器id", max_length=50, default='')
    temtime = models.DateTimeField(verbose_name="操作时间", default=timezone.now)
    detail = models.CharField(verbose_name="操作详情", max_length=50, default=0)

    def __str__(self):
        return self.userid


class TemperatureHistory(models.Model):
    temNo = models.CharField(verbose_name="感应器id", max_length=50, default='')
    temname = models.CharField(verbose_name="感应器名称", max_length=50, default='')
    temtime = models.DateTimeField(verbose_name="温度时间", default=timezone.now)
    temtem = models.CharField(verbose_name="温度", max_length=50, default=0)

    def __str__(self):
        return self.temname


class COtHistory(models.Model):
    coNo = models.CharField(verbose_name="感应器id", max_length=50, default='')
    coname = models.CharField(verbose_name="感应器名称", max_length=50, default='')
    cotime = models.DateTimeField(verbose_name="CO2时间", default=timezone.now)
    cotem = models.CharField(verbose_name="co2度", max_length=50, default=0)

    def __str__(self):
        return self.coname


class PMHistory(models.Model):
    pmNo = models.CharField(verbose_name="感应器id", max_length=50, default='')
    pmname = models.CharField(verbose_name="感应器名称", max_length=50, default='')
    pmtime = models.DateTimeField(verbose_name="PM2.5时间", default=timezone.now)
    pmtem = models.CharField(verbose_name="PM2.5度", max_length=50, default=0)

    def __str__(self):
        return self.pmname


class HumidityHistory(models.Model):
    humNo = models.CharField(verbose_name="感应器id", max_length=50, default='')
    humname = models.CharField(verbose_name="感应器名称", max_length=50, default='')
    humtime = models.DateTimeField(verbose_name="湿度时间", default=timezone.now)
    humtem = models.CharField(verbose_name="湿度", max_length=50, default=0)

    def __str__(self):
        return self.humname


class LigthHistory(models.Model):
    lightNo = models.CharField(verbose_name="感应器id",max_length=50,default='')
    lightname = models.CharField(verbose_name="感应器名称",max_length=50,default='')
    lighttime = models.DateTimeField(verbose_name="光照时间",default=timezone.now)
    lighttem = models.CharField(verbose_name="光照强度",max_length=50,default=0)

    def __str__(self):
        return self.lightname


class InviteHistory(models.Model):
    invite = models.ForeignKey(UserInfo, verbose_name="邀请人", related_name='invite')
    user = models.ForeignKey(UserInfo, verbose_name="用户", related_name='user')
    invitetime = models.DateTimeField(verbose_name="邀请时间", default=timezone.now)

    def __str__(self):
        return self.invite.username


class OpenCloseHistory(models.Model):
    machine = models.ForeignKey(Machine, verbose_name='设备')
    user = models.ForeignKey(UserInfo, verbose_name="用户")
    octime = models.DateTimeField(verbose_name="操作时间", default=timezone.now)
    detail = models.CharField(verbose_name="操作详情", max_length=50, default=0)

    def __str__(self):
        return self.detail



