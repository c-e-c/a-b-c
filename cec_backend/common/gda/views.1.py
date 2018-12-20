import json
from django.db import transaction
from rest_framework import viewsets, status, response
from rest_framework.decorators import action
from rest_framework.pagination import CursorPagination, LimitOffsetPagination
from rest_framework import mixins
from rest_framework.response import Response

from common.gda.mapping import ClassPackageMapping, SerializerPackageMapping

# Create your views here.


"""
    为每个用户添加token验证
"""
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


"""
#from django.contrib.auth.models import User
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
"""


def tableClass(tableName):
    """
        生成TableModel类
    """
    return getattr(
        __import__(ClassPackageMapping[tableName] +
                   ".models", fromlist=["models"]),
        tableName,
    )
    pass


def serializerClass(serializerName):
    """
        生成serializer类
    """
    return getattr(
        __import__(
            SerializerPackageMapping[serializerName] + ".serializers",
            fromlist=["serializers"],
        ),
        serializerName,
    )
    pass


class CommonResponse(Response):
    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=None,
    ):

        super(Response, self).__init__(None, status=status)

        self.data = data
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value
        pass


class StandardResultsSetPagination(CursorPagination):
    ordering = "pk"

    # def get_page_size(self, request):
    #     #todo
    #     pass

    # def get_paginated_response(self, data):
    #     #todo
    #     pass
    pass


class CommonRetrieveModelMixin(mixins.RetrieveModelMixin):
    def retrieve(self, request, *args, **kwargs):
        """
            type为表名（必选），
            props（可选）为要查询的列名数组
            {
                'type': 'xxx',
                'props': ['列名xxx', ],
            }
        """
        # 设置queryset
        params = request.query_params
        tableName = params.get("type")
        serializerName = tableName + "Serializer"

        Table = tableClass(tableName)
        self.queryset = Table.objects.all()

        # 设置serializer_class
        serializerName = tableName + "Serializer"
        self.serializer_class = serializerClass(serializerName)

        return super(CommonRetrieveModelMixin, self).retrieve(request, *args, **kwargs)


class CommonCreateModelMixin(mixins.CreateModelMixin):
    def _doCreate(self, *args, **kwargs):
        serializer = self.get_serializer(*args, **kwargs)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return serializer.data

    def create(self, request, *args, **kwargs):
        """
            type为表名（必选），
            record（更新、部分更新、插入必选，删除不需要）表的列值对
            {
                type: 'xxx',
                inserted: {'列名xxx': '列值xxx' ,'temp_pk':xxx}
            }
        """
        params = request.data
        tableName = params.get("type")
        serializerName = tableName + "Serializer"
        # 设置serializer_class
        self.serializer_class = serializerClass(serializerName)

        requestData = request.data.get("inserted", None)
        insertingData = []
        manyFlag = False
        if requestData is not None:
            if isinstance(requestData, str):
                insertingData = json.loads(requestData)
                manyFlag = True
            else:
                insertingData = requestData
                manyFlag = False
        else:
            pass

        kwargs["data"] = insertingData
        kwargs["many"] = manyFlag

        # 修改CreateModelMixin的create内容
        retval = self._doCreate(*args, **kwargs)
        headers = self.get_success_headers(retval)
        #######
        return response.Response(
            retval, status=status.HTTP_201_CREATED, headers=headers
        )


class CommonUpdateModelMixin(mixins.UpdateModelMixin):
    def __doUpdate(self, value, partial):
        # 修改UpdateModelMixin的update
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=value, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
            pass
        return serializer.data

    def update(self, request, *args, **kwargs):
        """
            type为表名（必选），
            record（更新、部分更新、插入必选，删除不需要）表的列值对
            {
                type: 'xxx',
                updated: {'列名xxx': '列值xxx' ,}
            }
        """
        # 设置queryset
        params = request.data
        tableName = params.get("type")
        Table = tableClass(tableName)
        self.queryset = Table.objects.all()

        # 设置serializer_class
        serializerName = tableName + "Serializer"
        self.serializer_class = serializerClass(serializerName)

        requestData = request.data.get("updated", False)
        updatingData = []
        manyFlag = False
        if requestData is not None:
            if isinstance(requestData, str):
                updatingData = json.loads(requestData)
                manyFlag = True
            else:
                updatingData = requestData
                manyFlag = False
        else:
            pass

        if manyFlag:
            retval = []
            for value in updatingData:
                self.kwargs["pk"] = value["pk"]
                partial = kwargs.pop("partial", True)  # 默认支持部分属性字段更新
                retval.append(self.__doUpdate(value, partial))
                pass
            return response.Response(retval)
        else:
            self.kwargs["pk"] = updatingData["pk"]
            partial = kwargs.pop("partial", True)  # 默认支持部分属性字段更新
            return response.Response(self.__doUpdate(value, partial))
        pass


class CommonDestroyModelMixin(mixins.DestroyModelMixin):
    def destroy(self, request, *args, **kwargs):
        """
            type为表名（必选），
            record（更新、部分更新、插入必选，删除不需要）表的列值对
            {
                type: 'xxx',
                removed: {'列名xxx': '列值xxx' ,}
            }
        """
        # 设置queryset
        params = request.data
        tableName = params.get("type")
        Table = tableClass(tableName)
        self.queryset = Table.objects.all()

        # 设置serializer_class
        serializerName = tableName + "Serializer"
        self.serializer_class = serializerClass(serializerName)

        requestData = request.data.get("removed", False)
        removingData = []
        manyFlag = False
        if requestData is not None:
            if isinstance(requestData, str):
                removingData = json.loads(requestData)
                manyFlag = True
            else:
                removingData = requestData
                manyFlag = False
        else:
            pass

        if manyFlag:
            for value in removingData:
                self.kwargs["pk"] = value
                super(CommonDestroyModelMixin, self).destroy(
                    self, request, *args, **kwargs
                )
                pass
        else:
            super(CommonDestroyModelMixin, self).destroy(
                self, request, *args, **kwargs)
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class CommonListModelMixin(mixins.ListModelMixin):
    def list(self, request, *args, **kwargs):
        """
        type为表名（必选）如'SysParamType'，
        props（可选）为要查询的列名数组
        filters（可选）为过滤条件数组，其中column为过滤的列，
            value为值，comparison为django查询的关键词如contains, exact等
        limit (可选) 10为每页10条记录，
            该参数是django-rest-framework的LimitOffsetPagination类的limit_query_param的值
        offset (可选) 5为从哪条记录开始查询
            该参数是django-rest-framework的LimitOffsetPagination类的offset_query_param的值
        {
            'type': 'xxx',
            'props': ['xxx', ],
            'filters': [{
                'prop': 'xxx',
                'value': 'xxx',
                'comparison': 'contains',
            }, ],
            'limit': '10',
            'offset': '5',
        }
        """
        params = self.request.query_params
        tableName = params.get("type")
        serializerName = tableName + "Serializer"

        # 设置queryset
        Table = tableClass(tableName)
        if params.get("filters") is not None:
            filters = json.loads(params.get("filters"))
            d = dict()
            for filter in filters:
                k = filter["prop"] + "__" + filter["comparison"]
                v = filter["value"]
                if filter["comparison"] == "isnull":
                    if filter["value"] == "True":
                        v = True
                    else:
                        v = False
                elif filter["comparison"] == "None":
                    v = None
                d[k] = v
            self.queryset = Table.objects.filter(**d).values(
                *json.loads(params.get("props"))
            )
        else:
            self.queryset = Table.objects.all().values(*json.loads(params.get("props")))

        # 修改ListModelMixin的list内容
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            return self.get_paginated_response(page)
        else:
            return CommonResponse(self.queryset)
        pass


class CommonViewSet(
    CommonListModelMixin,
    CommonRetrieveModelMixin,
    CommonCreateModelMixin,
    CommonUpdateModelMixin,
    CommonDestroyModelMixin,
    viewsets.GenericViewSet,
):
    # authentication_classes = (SessionAuthentication, BasicAuthentication,)
    # permission_classes = (AllowAny,)
    pagination_class = LimitOffsetPagination

    @action(methods=["post"], detail=False)
    def saveData(self, request, *args, **kwargs):
        """
            type为表名（必选），如SysParamType
            diffModel（必选）为差异模型资源序列,
            其中insert为插入的资源序列，update为修改的资源序列，remove为删除的资源id序列
            {
                'type': 'xxx',
                'inserted': [{'列名xxx': '列值xxx'},],
                'updated': [{'pk':'主键xxx', '列名xxx': '列值xxx'},],
                'removed': ['主键xxx',]
            }
        """
        params = request.data

        insertRds = None
        with transaction.atomic():
            if (
                params.get("inserted") is not None
                and len(json.loads(params.get("inserted"))) != 0
            ):
                insertRds = self.create(request, *args, **kwargs)
            if (
                params.get("updated") is not None
                and len(json.loads(params.get("updated"))) != 0
            ):
                self.update(request, *args, **kwargs)
            if (
                params.get("removed") is not None
                and len(json.loads(params.get("removed"))) != 0
            ):
                self.destroy(request, *args, **kwargs)
            pass
        if insertRds is not None:
            return response.Response(insertRds.data, status=status.HTTP_200_OK)
        else:
            return response.Response(status=status.HTTP_200_OK)
        pass

    @action(methods=["get"], detail=False)
    def multilist(self, request, *args, **kwargs):
        """
        type为表名（必选）如'SysParamType'，
        props（可选）为要查询的列名数组，如果是关联表的属性，则用外键+__+字段的方式
        filters（可选）为过滤条件数组，数组的一个对象type中prop为过滤的列，
            value为值，comparison为django查询的关键词如contains, exact等
            type为采用django多关联的方式，如"entity__blogs"表示Entity表中关联Blog表的记录
        {
            xxx:{
                'type': 'xxx',
                'props': ['xxx', ],
                'filters': [{
                    'prop': 'xxx',
                    'value': 'xxx',
                    'comparison': 'contains',
                }, ],
            },
        }
        """
        paramList = self.request.query_params

        retval = dict()
        for (paramKey, paramValue) in paramList.items():
            params = json.loads(paramValue)
            tableName = params.get("type")

            # 设置queryset
            Table = getattr(
                __import__(
                    ClassPackageMapping[tableName] + ".models", fromlist=["models"]
                ),
                tableName,
            )
            if params.get("filters") is not None:
                filters = params.get("filters")
                d = dict()
                for filter in filters:
                    k = filter["prop"] + "__" + filter["comparison"]
                    v = filter["value"]
                    if filter["comparison"] == "isnull":
                        if filter["value"] == "True":
                            v = True
                        else:
                            v = False
                    d[k] = v
                self.queryset = Table.objects.filter(**d)
            else:
                self.queryset = Table.objects.all()

            retval[paramKey] = self.queryset.values(*params.get("props"))
            pass

        return CommonResponse(retval)
        pass
