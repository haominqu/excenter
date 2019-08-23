# restful API
from rest_framework import serializers

# self_project
from .models import *


class UseHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = UseHistory
        fields = ('userid', 'macid', 'temtime', 'detail')


class TemperatureHistorySerializer(serializers.ModelSerializer):
    # temtime = serializers.SerializerMethodField('temtime_field')
    #
    # def temtime_field(self, obj):
    #     return obj.get_endpointnum_display()

    class Meta:
        model = TemperatureHistory
        fields = ('temNo', 'temname', 'temtime', 'temtem')


class COtHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = COtHistory
        fields = ('coNo', 'coname', 'cotime', 'cotem')


class PMHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PMHistory
        fields = ('pmNo', 'pmname', 'pmtime', 'pmtem')


class HumidityHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = HumidityHistory
        fields = ('humNo', 'humname', 'humtime', 'humtem')


class LigthHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = LigthHistory
        fields = ('lightNo', 'lightname', 'lighttime', 'lighttem')