###
from django.db import models
###
from common.gda.models import GeneralBaseModel

# Create your models here.

# 系统配置


class SysParamType(GeneralBaseModel):
    """
        系统参数类型
    """

    code = models.CharField(max_length=256, unique=True, verbose_name="编号")
    name = models.CharField(max_length=256, unique=True, verbose_name="名称")

    class Meta:
        verbose_name = "系统参数类型"


class SysParamValue(GeneralBaseModel):
    """
        系统参数值
    """

    code = models.CharField(max_length=256, unique=True, verbose_name="编号")
    name = models.CharField(max_length=256, unique=True, verbose_name="名称")
    param_type = models.ForeignKey(
        SysParamType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="系统参数值",
    )

    class Meta:
        verbose_name = "系统参数值"


class AppInstance(GeneralBaseModel):
    """
        应用实例
    """

    code = models.CharField(max_length=256, unique=True, verbose_name="编号")
    name = models.CharField(max_length=256, unique=True, verbose_name="名称")
    app_module = models.IntegerField(
        blank=True, null=True, verbose_name="应用模块")
    # app_module = models.ForeignKey(
    #     SysParamValue,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     verbose_name="应用模块",
    # )

    class Meta:
        verbose_name = "应用实例"


class BizParamType(GeneralBaseModel):
    """
        业务参数类型
    """

    code = models.CharField(max_length=256, unique=True, verbose_name="编号")
    name = models.CharField(max_length=256, unique=True, verbose_name="名称")

    class Meta:
        verbose_name = "业务参数类型"


# 用户配置
class BizParamValue(GeneralBaseModel):
    """
        业务参数值
    """

    code = models.CharField(max_length=256, unique=True, verbose_name="编号")
    name = models.CharField(max_length=256, unique=True, verbose_name="名称")
    biz_module = models.IntegerField(
        blank=True, null=True, verbose_name="业务模块")
    # biz_module = models.ForeignKey(
    #     SysParamValue,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     related_name="biz_module",
    #     verbose_name="业务模块",
    # )
    app_instance = models.IntegerField(
        blank=True, null=True, verbose_name="所属应用")
    # app_instance = models.ForeignKey(
    #     AppInstance,
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     verbose_name="所属应用",
    # )
    param_type = models.ForeignKey(
        BizParamType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="业务参数类型",
    )

    class Meta:
        verbose_name = "业务参数值"


# class CCPAMapper(models.Model):
#     """
#         汉字字母映射表
#     """

#     chinese_character = models.CharField(max_length=256, unique=True, verbose_name="汉字")
#     phonetic_alphabet = models.CharField(max_length=256, verbose_name="拼音字母")

#     class Meta:
#         verbose_name = "汉字字母映射表"


########## 应用表 ##########


# class BizParamSetting(SysBaseModel):
#     '''
#         业务参数设置
#     '''
#     name = models.CharField(
#         max_length=256, verbose_name='名称')

#     value = models.CharField(
#         max_length=256, verbose_name='设置值')
#     value_unit = models.CharField(
#         max_length=256, verbose_name='设置值单位')

#     param_type = models.ForeignKey(
#         'BizParamType', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='业务参数类型')

#     # todo 需要与相关表做关联
#     # belong_to = models.IntegerField(
#     #     null=True, blank=True, verbose_name='所属业务对象')

#     class Meta:
#         verbose_name = '业务参数设置'


# class BizPropertyValue(SysBaseModel):
#     '''
#         业务属性应用
#     '''
#     biz_property = models.ForeignKey(
#         'BizProperty', on_delete=models.CASCADE, verbose_name='业务属性')

#     value = models.CharField(
#         max_length=256, verbose_name='设置值')
#     value_unit = models.CharField(
#         max_length=256, null=True, blank=True, verbose_name='单位')

#     class Meta:
#         verbose_name = '业务属性应用'


########## 定义表 ##########


# class BizClass(SysExtModel):
#     '''
#         业务类型
#     '''
#     class Meta:
#         verbose_name = '业务类型'


# class BizProperty(SysExtModel):
#     '''
#         业务属性
#     '''
#     value_type = models.ForeignKey(
#         'SysParamValue', related_name='value_type_bizpropertyset', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='属性值类型')
#     value_length = models.IntegerField(verbose_name='属性值长度')
#     value_scale = models.IntegerField(
#         null=True, blank=True, verbose_name='属性值精度')
#     value_source = models.ForeignKey(
#         'SysParamValue', on_delete=models.SET_NULL, null=True, blank=True, related_name='value_source_bizpropertyset', verbose_name='属性值来源')  # 用户输入还是系统参数值
#     default_value = models.CharField(
#         max_length=256, null=True, blank=True, verbose_name='默认值')
#     required_flag = models.ForeignKey(
#         'SysParamValue', on_delete=models.SET_NULL, null=True, blank=True, related_name='required_flag_bizpropertyset', verbose_name='必填标志')

#     biz_class = models.ForeignKey(
#         BizClass, on_delete=models.CASCADE, verbose_name='业务类型')

#     class Meta:
#         verbose_name = '业务属性'
