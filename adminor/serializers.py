# restful API
from rest_framework import serializers

# django
from django.conf import settings

# self_project
from userinfo.models import *

class UserBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('id', 'username', 'role', 'is_active')


class StaffSerializer(serializers.ModelSerializer):

    user = UserBaseSerializer(many=False, read_only=True)

    face_picture = serializers.SerializerMethodField('face_picture_field')

    def face_picture_field(self, obj):
        return settings.BASE_URL + "/media" + str(obj.face_picture)

    class Meta:
        model = UserDetail
        fields = ('user', 'realname', 'staff_code', 'face_picture', 'position', 'department')



class GuestSerializer(serializers.ModelSerializer):

    user = UserBaseSerializer(many=False, read_only=True)

    invite = serializers.SerializerMethodField('invite_field')
    def invite_field(self, obj):
        invite_id = obj.invite.id
        user = UserDetail.objects.filter(user_id=invite_id)
        return user[0].realname

    audit_status = serializers.SerializerMethodField('audit_field')
    def audit_field(self, obj):
        return obj.audit_status

    face_picture = serializers.SerializerMethodField('face_picture_field')
    def face_picture_field(self, obj):
        return settings.BASE_URL + "/media/" + str(obj.face_picture)

    class Meta:
        model = Guest
        fields = ('user', 'realname', 'invite', 'audit_status', 'face_picture', 'position', 'department')