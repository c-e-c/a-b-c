"""serializers"""
from rest_framework import serializers

from common.gda.serializers import DynamicFieldsModelSerializer
from common.party.models import *


class PartyTypeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = PartyType
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer


class PartySerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Party
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer


class OrganizationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer


class EmployeeSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer


class IndividualMemberSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = IndividualMember
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer


class CorporateMemberSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = CorporateMember
        fields = "__all__"
        list_serializer_class = serializers.ListSerializer
