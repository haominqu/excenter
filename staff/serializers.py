# restful API
from rest_framework import serializers

# self_project
from userinfo.serializers import UserSerializer
from userinfo.models import UserDetail


class StaffSerializer(serializers.ModelSerializer):

    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = UserDetail
        fields = ('user', 'realname', 'staff_code', 'position', 'department')