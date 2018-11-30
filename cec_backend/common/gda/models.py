from django.db import models

# Create your models here.


class GeneralBaseModel(models.Model):
    """
        abstract base model
    """

    description = models.CharField(
        max_length=4096, null=True, blank=True, verbose_name="描述"
    )
    remark = models.CharField(
        max_length=4096, null=True, blank=True, verbose_name="备注")
    sn = models.CharField(max_length=256, null=True,
                          blank=True, verbose_name="排序号")
    valid_flag = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        choices=(("Y", "是"), ("N", "否")),
        verbose_name="有效标志",
    )
    created_man = models.CharField(
        max_length=256, null=True, blank=True, verbose_name="创建人"
    )
    created_datetime = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name="创建时间"
    )
    modified_man = models.CharField(
        max_length=256, null=True, blank=True, verbose_name="修改人"
    )
    modified_datetime = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name="修改时间"
    )

    # def __str__(self):
    #     return '%s(%s)' % (self.name, self.code)

    class Meta:
        abstract = True

    pass
