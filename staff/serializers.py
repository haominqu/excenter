# restful API
from rest_framework import serializers

# self_project
from userinfo.serializers import UserSerializer
from userinfo.models import UserInfo, UserDetail, Guest

class UserBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('id', 'username', 'is_active')


class StaffSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = UserDetail
        fields = ('user', 'realname', 'staff_code', 'position', 'department')



class GuestSerializer(serializers.ModelSerializer):

    user = UserBaseSerializer(many=False, read_only=True)


    audit_status = serializers.SerializerMethodField('audit_field')
    def audit_field(self, obj):
        return obj.audit_status


    class Meta:
        model = Guest
        fields = ('user', 'realname', 'audit_status', 'face_picture', 'position', 'department')
