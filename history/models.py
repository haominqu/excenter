from django.db import models

# Create your models here.
class UseHistory(models.Model):
    pass


class MachineHistory(models.Model):
    pass


class TemperatureHistory(models.Model):
    pass


class COtHistory(models.Model):
    pass


class PMHistory(models.Model):
    pass


class HumidityHistory(models.Model):
    pass


class LigthHistory(models.Model):
    lightNo = models.CharField(verbose_name="感应器id",max_length=50,default='')
    lightname = models.CharField(verbose_name="感应器名称",max_length=50,default='')
    lighttime = models.DateTimeField(verbose_name="光照时间",auto_now_add=True)
    lighttem = models.CharField(verbose_name="光照强度",max_length=50,default=0)

    def __str__(self):
        return self.lightname





