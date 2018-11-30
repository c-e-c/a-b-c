
"""serializers"""
from rest_framework import serializers
from common.gda.serializers import DynamicFieldsModelSerializer
from common.system.models import *

# 需要根据业务实现


class SysParamTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = SysParamType
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer


class SysParamValueSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = SysParamValue
        fields = "__all__"


class AppInstanceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = AppInstance
        fields = "__all__"


class BizParamTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = BizParamType
        fields = "__all__"


class BizParamValueSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = BizParamValue
        fields = "__all__"


# class CCPAMapperSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = CCPAMapper
#         fields = "__all__"

# class BizParamSettingSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = BizParamSetting
#         fields = '__all__'


# class BizPropertyValueSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = BizPropertyValue
#         fields = '__all__'


# class BizClassSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = BizClass
#         fields = '__all__'


# class BizPropertySerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = BizProperty
#         fields = '__all__'
