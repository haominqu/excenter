from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UseHistory)
admin.site.register(TemperatureHistory)
admin.site.register(COtHistory)
admin.site.register(PMHistory)
admin.site.register(HumidityHistory)
admin.site.register(LigthHistory)

