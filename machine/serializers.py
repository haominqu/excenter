# restful API
from rest_framework import serializers

# selfproject
from .models import *

class MachineSerializer(serializers.ModelSerializer):

    gate = serializers.SerializerMethodField('gate_field')

    def gate_field(self, obj):
        return obj.gate.gw_name

    class Meta:
        model = Machine
        fields = ('id', 'mac_name', 'mac_devID', 'mac_type', 'gate', 'scene', 'mac_ctype')


class ControlMacSerializer(serializers.ModelSerializer):

    mac = MachineSerializer(many=False, read_only=True)

    endpointnum = serializers.SerializerMethodField('endpointnum_field')

    def endpointnum_field(self, obj):
        return obj.get_endpointnum_display()
    # def mac(self, obj):
    #     return obj.mac.mac_name

    class Meta:
        model = ControlMac
        fields = ('mac', 'endpointnum', 'mac_status')

