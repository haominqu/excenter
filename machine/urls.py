from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'lamp/', Lamp.as_view(), name='lamp'),
    url(r'controll/list/$', ControllMachine.as_view(), name='controll_machine'),  # 可控设备列表
    url(r'sensor/list/$', SensorMachine.as_view(), name='sensor_machine'),  # 感应器设备列表

]
