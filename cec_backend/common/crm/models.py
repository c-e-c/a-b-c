from django.db import models

# Create your models here.


# class ParamBaseModel(models.Model):
#     '''
#         参数的抽象基类
#     '''
#     name = models.CharField(
#         max_length=256, null=True, blank=True, verbose_name='名称')
#     code = models.CharField(
#         max_length=256, unique=True, verbose_name='编号')

#     def __str__(self):
#         return '%s(%s)' % (self.name, self.code)

#     class Meta:
#         abstract = True


# class BizParamType(ParamBaseModel):
#     '''
#         业务参数类型
#     '''
#     type_level = models.IntegerField(verbose_name='级别')

#     belong_to = models.IntegerField(
#         null=True, blank=True, verbose_name='所属对象')

#     class Meta:
#         verbose_name = '业务参数类型'
