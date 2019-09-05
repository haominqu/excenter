from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'regist/number/$', RegistNumber.as_view(), name='regist_number'),
    url(r'temhum/data/$', TemperHumView.as_view(), name='temhum_data'),
    url(r'pmco/data/$', PMCO2View.as_view(), name='pmco_data'),
]
