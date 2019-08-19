from django.contrib import admin
from .models import Gate, Machine, ControlMac,MacSetting,Scene
# Register your models here.

admin.site.register(Gate)
admin.site.register(Machine)
admin.site.register(ControlMac)
admin.site.register(MacSetting)
admin.site.register(Scene)

