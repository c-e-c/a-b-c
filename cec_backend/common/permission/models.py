from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from common.gda.models import GeneralBaseModel

# Create your models here.


class Account(GeneralBaseModel):
    """
        账号
    """

    """
     user:  id | password | last_login | is_superuser | username | first_name
         | email | is_staff | is_active | date_joined | last_name
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 外键关联system模块BizParamValue表
    account_type = models.IntegerField(
        blank=True, null=True, verbose_name="账号类型")
    # 外键关联member模块member表
    member = models.IntegerField(blank=True, null=True, verbose_name="会员")
    head_img = models.CharField(
        max_length=4096, blank=True, null=True, verbose_name="头像"
    )
    email_binding_flag = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        choices=(("Y", "是"), ("N", "否")),
        verbose_name="邮箱绑定标志",
    )
    phone_number = models.CharField(max_length=256, blank=True,
                                    null=True, verbose_name="手机号")
    phone_binding_flag = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        choices=(("Y", "是"), ("N", "否")),
        verbose_name="手机号绑定标志",
    )
    qq_openid = models.CharField(
        max_length=4096, blank=True, null=True, verbose_name="QQopenid"
    )
    qq_binding_flag = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        choices=(("Y", "是"), ("N", "否")),
        verbose_name="QQ绑定标志",
    )

    wechat_openid = models.CharField(
        max_length=4096, blank=True, null=True, verbose_name="微信openid"
    )
    wechat_binding_flag = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        choices=(("Y", "是"), ("N", "否")),
        verbose_name="微信绑定标志",
    )
    current_login_ip = models.CharField(
        max_length=256, blank=True, null=True, verbose_name="当前登录IP"
    )
    current_login_type = models.CharField(
        max_length=256, blank=True, null=True, verbose_name="当前登录类型"
    )

    class Meta:
        verbose_name = "账号"


class Role(GeneralBaseModel):
    """
        角色
    """

    """
     group:  id | name 
    """

    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    # 外键关联system模块SysParamValue表
    role_type = models.IntegerField(blank=True, null=True, verbose_name="角色类型")

    class Meta:
        verbose_name = "角色"


class ControlObject(GeneralBaseModel):
    """
        控制对象
    """

    code = models.CharField(max_length=256, unique=True, verbose_name="编号")
    name = models.CharField(max_length=256, unique=True, verbose_name="名称")

    # 外键关联system模块SysParamValue表
    control_object_type = models.IntegerField(
        blank=True, null=True, verbose_name="控制对象类型"
    )

    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="child_set",
    )

    class Meta:
        verbose_name = "控制对象"


class ControlPolicy(GeneralBaseModel):
    """
        控制策略
    """

    """
     permission:  id | content_type_id | codename | name 
    """
    permission = models.OneToOneField(Permission, on_delete=models.CASCADE)
    # 外键关联system模块SysParamValue表
    control_policy_type = models.IntegerField(
        blank=True, null=True, verbose_name="控制策略类型"
    )

    control_object = models.ForeignKey(
        ControlObject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="控制对象",
    )

    class Meta:
        verbose_name = "控制策略"
