# restful API
from rest_framework import serializers

# self_project
from .models import *
from userinfo.models import UserDetail, Guest


class UseHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = UseHistory
        fields = ('userid', 'macid', 'temtime', 'detail')


class InviteHistorySerializer(serializers.ModelSerializer):

    invite = serializers.SerializerMethodField('invite_field')
    def invite_field(self, obj):
        invite_id = obj.invite.id
        user = UserDetail.objects.filter(user_id=invite_id)
        return user[0].realname

    user = serializers.SerializerMethodField('user_field')

    def user_field(self, obj):
        user_id = obj.user.id
        user = Guest.objects.filter(user_id=user_id)
        return user[0].realname

    class Meta:
        model = InviteHistory
        fields = ('invite', 'user', 'invitetime')


class OpenCloseHistorySerializer(serializers.ModelSerializer):

    machine = serializers.SerializerMethodField('machine_field')

    def machine_field(self, obj):
        return obj.machine.mac_name

    user = serializers.SerializerMethodField('user_field')

    def user_field(self, obj):
        user_id = obj.user.id
        user = Guest.objects.filter(user_id=user_id)
        return user[0].realname

    class Meta:
        model = OpenCloseHistory
        fields = ('machine', 'user', 'octime', 'detail')


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