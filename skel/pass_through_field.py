from rest_framework.fields import Field


class PassThroughField(Field):
    def to_internal_value(self, data):
        return data

    def to_representation(self, obj):
        return obj
