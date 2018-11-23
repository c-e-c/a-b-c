"""serializers"""
from rest_framework import serializers

from common.gda.serializers import DynamicFieldsModelSerializer
from common.member.models import *


class MemberSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer
