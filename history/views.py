# restful API
from rest_framework.views import APIView

# django
from django.http import JsonResponse
from userinfo.permissions import IsAdmin, login_decorator
from django.utils.decorators import method_decorator

# self_project
from .models import *
from django.shortcuts import render
from .serializers import *

# Create your views here.


class UseHistoryView(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)

    def get(self, request, *args, **kwargs):
        history = UseHistory.objects.all()
        history_se = UseHistorySerializer(history, many=True)
        result = True
        data = history_se.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class InviteHistoryView(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)

    def get(self, request, *args, **kwargs):
        history = InviteHistory.objects.all()
        history_se = InviteHistorySerializer(history, many=True)
        result = True
        data = history_se.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class OpenCloseHistoryView(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)

    def get(self, request, *args, **kwargs):
        history = OpenCloseHistory.objects.all()
        history_se = OpenCloseHistorySerializer(history, many=True)
        result = True
        data = history_se.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class TemperatureHistoryView(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        history = TemperatureHistory.objects.all()
        history_se = TemperatureHistorySerializer(history, many=True)
        result = True
        data = history_se.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class COtHistoryView(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        history = COtHistory.objects.all()
        history_se = COtHistorySerializer(history, many=True)
        result = True
        data = history_se.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class PMHistoryView(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        history = PMHistory.objects.all()
        history_se = PMHistorySerializer(history, many=True)
        result = True
        data = history_se.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class HumidityHistoryView(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        history = HumidityHistory.objects.all()
        history_se = HumidityHistorySerializer(history, many=True)
        result = True
        data = history_se.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})


class LigthHistoryView(APIView):
    permission_classes = (
        IsAdmin,
    )

    @method_decorator(login_decorator)
    def get(self, request, *args, **kwargs):
        history = LigthHistory.objects.all()
        history_se = LigthHistorySerializer(history, many=True)
        result = True
        data = history_se.data
        error = ""
        return JsonResponse({"result": result, "data": data, "error": error})