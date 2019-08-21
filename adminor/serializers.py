# restful API
from rest_framework import serializers

# self_project
from userinfo.models import *

class UserBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('id', 'username', 'role', 'is_active')


class StaffSerializer(serializers.ModelSerializer):

    user = UserBaseSerializer(many=False, read_only=True)

    class Meta:
        model = UserDetail
        fields = ('user', 'realname', 'staff_code', 'face_picture', 'position', 'department')



class GuestSerializer(serializers.ModelSerializer):

    user = UserBaseSerializer(many=False, read_only=True)

    invite = serializers.SerializerMethodField('invite_field')
    def invite_field(self, obj):
        return obj.user.username

    audit_status = serializers.SerializerMethodField('audit_field')
    def audit_field(self, obj):
        return obj.audit_status


    class Meta:
        model = Guest
        fields = ('user', 'realname', 'invite', 'audit_status', 'face_picture', 'position', 'department')