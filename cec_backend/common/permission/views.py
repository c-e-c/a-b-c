
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from rest_framework.decorators import action

from common.gda.views import CommonViewSet, CommonCreateModelMixin
from common.permission.models import *


"""
    创建django的User对象时同时创建Account对象
"""


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        pass
    #     Account.objects.create(user=instance)
    pass


"""
    创建django的Permission对象时同时创建ControlPolicy对象
"""


@receiver(post_save, sender=Permission)
def create_permission(sender, instance=None, created=False, **kwargs):
    if created:
        ControlPolicy.objects.create(permission=instance)


"""
    创建django的Group对象时同时创建Role对象
"""


@receiver(post_save, sender=Group)
def create_group(sender, instance=None, created=False, **kwargs):
    if created:
        Role.objects.create(group=instance)


class PermissionViewSet(CommonViewSet):
    def _doCreate(self, *args, **kwargs):
        for record in kwargs["data"]:
            fact_fields = dict()
            columns = User._meta.fields
            for iter in columns:
                v = record.get(iter.column)
                if v is not None:
                    fact_fields[iter.column] = v
                pass
            u = User(**fact_fields)
            u.save()
            record["user"] = u.pk
            pass

        return super(PermissionViewSet, self)._doCreate(*args, **kwargs)

    @action(methods=["post"], detail=False)
    def saveData(self, request, *args, **kwargs):

        post_save.disconnect(create_user)

        retval = super(PermissionViewSet, self).saveData(
            request, *args, **kwargs)

        post_save.connect(create_user, settings.AUTH_USER_MODEL)

        return retval
        pass
