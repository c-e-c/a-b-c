
"""serializers"""
import json

from rest_framework import serializers


"""
    fields 包含要设置的字段
    fields = ('region_code', 'region_name',)
    __all__表示全部
    fields = '__all__'

    exclude 包含不设置的字段
    exclude = ('region_name',)

    dept=1表示要获取外键所有字段,如下所示
    [
        {
            "id": 1,
            "priority": 10,
            "role": {
                "id": 1,
                "department": "researcher"
            }
        }
    ]

    read_only_fields 只读字段
    read_only_fields = ('account_name',)

    """


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'props' arg up to the superclass
        # props = kwargs.pop('xxx', None)

        if kwargs["context"]["view"].action == "list":
            props = json.loads(
                kwargs["context"]["request"].query_params.get("props", None)
            )
            if props is not None:
                # Drop any fields that are not specified in the `fields` argument.
                allowed = set(props)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
        pass

    pk = serializers.IntegerField(required=False)
    pass
