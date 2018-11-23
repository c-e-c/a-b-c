from django.db import models

from common.gda.models import GeneralBaseModel


class Party(GeneralBaseModel):
    """
        当事人
    """

    code = models.CharField(max_length=256, blank=True,
                            null=True, verbose_name="编号")
    name = models.CharField(max_length=256, blank=True,
                            null=True, verbose_name="名称")

    # 外键关联system模块BizParamValue表
    party_type = models.IntegerField(
        blank=True, null=True, verbose_name="当事人类型")

    class Meta:
        verbose_name = "当事人"


# class Organization(Party):
#     """
#         组织
#     """

#     parent = models.ForeignKey(
#         "self",
#         on_delete=models.SET_NULL,
#         blank=True,
#         null=True,
#         # related_name="child_set",
#         verbose_name="上级",
#     )

#     org_level = models.ForeignKey(
#         "system.BizParamValue",
#         on_delete=models.SET_NULL,
#         blank=True,
#         null=True,
#         # related_name="organizations_set",
#         verbose_name="组织级别",
#     )

#     class Meta:
#         verbose_name = "组织"


# class Employee(Party):
#     """
#         员工
#     """

#     org = models.ForeignKey(
#         "Organization",
#         on_delete=models.SET_NULL,
#         blank=True,
#         null=True,
#         # related_name="organization_set",
#         verbose_name="组织机构",
#     )

#     working_state = models.ForeignKey(
#         "system.BizParamValue",
#         on_delete=models.SET_NULL,
#         blank=True,
#         null=True,
#         # related_name="employees_set",
#         verbose_name="在岗状态",
#     )

#     class Meta:
#         verbose_name = "员工"


# class IndividualMember(Party):
#     """
#         个人会员
#     """

#     class Meta:
#         verbose_name = "个人会员"


# class CorporateMember(Party):
#     """
#         企业会员
#     """

#     class Meta:
#         verbose_name = "企业会员"
