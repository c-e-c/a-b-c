
"""serializers"""
from rest_framework import serializers

from common.gda.serializers import DynamicFieldsModelSerializer
from common.permission.models import *

# 需要根据业务实现


class AccountSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer


class RoleSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer


class ControlPolicySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ControlPolicy
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer


class ControlObjectSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = ControlObject
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer
