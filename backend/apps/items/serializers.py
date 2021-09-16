from rest_framework import serializers
from . import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        # fields = ('id', 'name', 'content', 'created_at', 'updated_at',)
        fields = '__all__'
