from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'lamp/', Lamp.as_view(), name='lamp'),
    url(r'curtain/', Curtain.as_view(), name='curtain'),
    url(r'controll/list/$', ControllMachine.as_view(), name='controll_machine'),  # 可控设备列表
    url(r'controllm/list/$', ControllMachineM.as_view(), name='controllm_machine'),  # 可控设备列表
    url(r'sensor/list/$', SensorMachine.as_view(), name='sensor_machine'),  # 感应器设备列表
    url(r'machine/active/$', MachineActive.as_view(), name='machine_active'),  # 设备激活、停用
    url(r'alter/mac_name/$', AlterMachineName.as_view(), name='alter_mac_name'),  # 修改设备名称
    url(r'mac/mode/$', MacModeView.as_view(), name='mac_mode'),  # 设备模式

]
