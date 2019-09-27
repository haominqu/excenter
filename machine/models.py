from django.db import models

ENDPOINT_CHOICES=(
    (1,'No.1'),
    (2,'No.2'),
    (3,'No.3'),
    (4,'No.4'),
)

MACMODE_CHOICES=(
    (1,'自动'),
    (2,'手动'),
)

SCE_TYPE_CHOICES = (
    (0,'感应'),
    (1,'触发'),
    (2,'数据'),
)

ACTIVE_CHOICES = (
    (0, '未激活'),
    (1, '激活'),
    (2, '停用'),
)

STATUS_CHOICES = (
    (0, '故障'),
    (1, '运行中'),
    (2, '已停用'),
    (3, '检修中'),
)
MAC_KIND = (
    (0, '可控'),
    (1, '感应'),
    (2, '温度'),
    (3, '湿度'),
    (4, '光照'),
    (5, 'CO2'),
    (6, '电力'),
    (7, 'PM2.5'),
)
# Create your models here.


class Gate(models.Model):
    gw_name = models.CharField(verbose_name='网关名称', max_length=50, null=False)
    gw_gwID = models.CharField(verbose_name='网关ID', max_length=50, null=False)
    ad_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.gw_name


class Scene(models.Model):
    sc_name = models.CharField(verbose_name='场景名称', max_length=50, null=False)

    def __str__(self):
        return self.sc_name


class Machine(models.Model):
    mac_name = models.CharField(verbose_name='设备名称', max_length=50, null=False)
    mac_devID = models.CharField(verbose_name='设备码', max_length=50, null=False)
    mac_type = models.CharField(verbose_name='设备类型', max_length=50, null=False)
    gate = models.ForeignKey(Gate,verbose_name="网关")
    scene = models.ForeignKey(Scene,verbose_name="场景")
    mac_ctype = models.IntegerField(verbose_name='设备属性', choices=SCE_TYPE_CHOICES, default=0)
    is_active = models.IntegerField(verbose_name='激活状态', choices=ACTIVE_CHOICES, default=1)
    status = models.IntegerField(verbose_name='设备状态', choices=STATUS_CHOICES, default=1)
    kind = models.IntegerField(verbose_name='设备种类', choices=MAC_KIND, default=0)


    def __str__(self):
        return self.mac_name

# mac_status 0/off 1/on
class ControlMac(models.Model):
    mac = models.OneToOneField(Machine,verbose_name='设备')
    endpointnum = models.IntegerField(verbose_name='开关路号',choices=ENDPOINT_CHOICES,default=1)
    mac_status = models.IntegerField(verbose_name='开关状态', null=True, blank=True)
    temperature = models.CharField(verbose_name='温度光感', null=True, blank=True, max_length=20)

    def __str__(self):
        return self.mac.mac_name


class MacSetting(models.Model):
    mac_mode = models.IntegerField(verbose_name='模式',choices=MACMODE_CHOICES,default=0)

    def __str__(self):
        print(self.mac_mode)
        if self.mac_mode == 1:
            return '自动'
        else:
            return '手动'




# class SensorMac(models.Model):
#     mac = models.OneToOneField(Machine, verbose_name='设备')
#     sen_value = models.IntegerField(verbose_name='设备状态数')
#
#     def __str__(self):
#         return self.mac.mac_name
