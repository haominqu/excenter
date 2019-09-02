from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'record/use/$', UseHistoryView.as_view(), name='use_record'),
    url(r'record/invite/$', InviteHistoryView.as_view(), name='invite_record'),
    url(r'record/access/$', AccessHistoryView.as_view(), name='access_record'),
    url(r'record/tempera/$', TemperatureHistoryView.as_view(), name='tempera_record'),
    url(r'record/cot/$', COtHistoryView.as_view(), name='cot_record'),
    url(r'record/pm/$', PMHistoryView.as_view(), name='pm_record'),
    url(r'record/humid/$', HumidityHistoryView.as_view(), name='humid_record'),
    url(r'record/ligth/$', LigthHistoryView.as_view(), name='ligth_record'),

]