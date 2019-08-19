# restful API
from rest_framework import serializers

# selfproject
from .models import *

class UserSerializer(serializers.ModelSerializer):

    role = serializers.SerializerMethodField('role_field')
    def role_field(self, obj):
        return obj.get_role_display()

    class Meta:
        model = UserInfo
        fields = ('username', 'role')


class StaffSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = UserDetail
        fields = ('realname', 'staff_code', 'position', 'department')



class GuestSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)

    invite = serializers.SerializerMethodField('invite_field')
    def invite_field(self, obj):
        return obj.user

    audit_status = serializers.SerializerMethodField('audit_field')
    def audit_field(self, obj):
        return obj.get_audit_status_display()


    class Meta:
        model = Guest
        fields = ('user', 'realname', 'invite', 'audit_status')