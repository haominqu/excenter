from django.contrib import admin
from .models import *

# Register your models here.

class TemperatureHistoryAdmin(admin.ModelAdmin):
    list_display=('id', 'temname', 'temtime', 'temtem')

class COtHistoryAdmin(admin.ModelAdmin):
    list_display=('id', 'coname', 'cotime', 'cotem')

class PMHistoryAdmin(admin.ModelAdmin):
    list_display=('id', 'pmname', 'pmtime', 'pmtem')

class HumidityHistoryAdmin(admin.ModelAdmin):
    list_display=('id', 'humname', 'humtime', 'humtem')

class LigthHistoryAdmin(admin.ModelAdmin):
    list_display=('id', 'lightname', 'lighttime', 'lighttem')

class ElectHistoryAdmin(admin.ModelAdmin):
    list_display=('id', 'electname', 'electttime', 'electtem')


admin.site.register(UseHistory)
admin.site.register(TemperatureHistory,TemperatureHistoryAdmin)
admin.site.register(COtHistory,COtHistoryAdmin)
admin.site.register(PMHistory,PMHistoryAdmin)
admin.site.register(HumidityHistory,HumidityHistoryAdmin)
admin.site.register(LigthHistory,LigthHistoryAdmin)
admin.site.register(InviteHistory)
admin.site.register(ElectHistory,ElectHistoryAdmin)
admin.site.register(AccessHistory)