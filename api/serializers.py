from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' 

#version 13djan