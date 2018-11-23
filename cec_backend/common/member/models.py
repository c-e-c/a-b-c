from django.db import models

from common.gda.models import GeneralBaseModel


class Member(GeneralBaseModel):
    """
        会员
    """

    code = models.CharField(max_length=256, blank=True,
                            null=True, verbose_name="会员编号")
    name = models.CharField(max_length=256, blank=True,
                            null=True, verbose_name="会员名称")

    # 外键关联system模块BizParamValue表
    level = models.IntegerField(
        blank=True, null=True, verbose_name="会员等级")

    # 外键关联system模块BizParamValue表
    member_type = models.IntegerField(
        blank=True, null=True, verbose_name="会员类型")

    # 外键关联party模块party表
    party = models.IntegerField(
        blank=True, null=True, verbose_name="当事人")

    # party = models.ForeignKey(
    #     "party.Party",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     # related_name="party_set",
    #     verbose_name="当事人",
    # )

    class Meta:
        verbose_name = "会员"
