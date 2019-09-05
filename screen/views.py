# restful API
from rest_framework.views import APIView

# django
from django.http import JsonResponse
from django.db.models import Avg

# self_project
from history.models import *
from userinfo.models import Guest

# base
import time
import datetime

# Create your views here.

class RegistNumber(APIView):

    def get(self, request):
        guest = Guest.objects.all()
        if not guest:
            result = False
            data = ""
            error = ""
            return JsonResponse({"result": result, "data": data, "error": error})
        guest_count = guest.count()
        result = True
        data = guest_count
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class TemperHumView(APIView):

    def get(self, request):
        now_date = datetime.date.today()
        date_list = []
        for i in range(0, 7):
            oneday = datetime.timedelta(days=i)
            day = now_date - oneday
            date_list.append(day)
        seven_days = sorted(date_list)
        # seven_days_ago = datetime.date.today() + datetime.timedelta(days=-6)
        # tempers = TemperatureHistory.objects.filter(temtime__range=[seven_days_ago, now_date+datetime.timedelta(days=1)])
        # date_list = []
        # for temper in tempers:
        #     date_list.append(temper.temtime.date())
        # no_repeat_date = list(set(date_list))
        # seven_days = sorted(no_repeat_date)
        tem_data = []
        hum_data = []
        for per_date in seven_days:
            avg_tem = TemperatureHistory.objects.filter(temtime__date=per_date).aggregate(Avg("temtem"))
            avg_hum = HumidityHistory.objects.filter(humtime__date=per_date).aggregate(Avg("humtem"))
            tem_data.append(avg_tem['temtem__avg'])
            hum_data.append(avg_hum['humtem__avg'])
        data = {}
        data['date'] = seven_days
        data['tem_data'] = tem_data
        data['hum_data'] = hum_data
        result = True
        data = data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})



class PMCO2View(APIView):

    def get(self, request):
        now_date = datetime.date.today()
        date_list = []
        for i in range(0, 100):
            oneday = datetime.timedelta(days=i)
            day = now_date - oneday
            date_list.append(day)
        seven_days = sorted(date_list)
        pm_data = []
        co2_data = []
        for per_date in seven_days:
            avg_pm = PMHistory.objects.filter(pmtime__date=per_date).aggregate(Avg("pmtem"))
            avg_co2 = COtHistory.objects.filter(cotime__date=per_date).aggregate(Avg("cotem"))
            pm_data.append(avg_pm['pmtem__avg'])
            co2_data.append(avg_co2['cotem__avg'])
        data = {}
        data['date'] = seven_days
        data['pm_data'] = pm_data
        data['co2_data'] = co2_data
        result = True
        data = data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})
