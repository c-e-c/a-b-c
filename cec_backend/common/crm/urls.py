###
from django.conf.urls import url, include

import rest_framework.authtoken.views
import rest_framework.routers
import rest_framework.urlpatterns
###
import common.crm.views
###


# 关于URL使用说明
# 如果添加了正在使用的url请放在正在使用区

router = rest_framework.routers.SimpleRouter()  # trailing_slash=False
router.register(r'crm', common.crm.views.CRMViewSet, 'crminfo')

urlpatterns = {
    url(r'^', include(router.urls)),
}


urlpatterns = rest_framework.urlpatterns.format_suffix_patterns(urlpatterns)
