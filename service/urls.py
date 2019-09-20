from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'', DhuiView.as_view(), name='dahui_face'),  # 达辉人脸

]