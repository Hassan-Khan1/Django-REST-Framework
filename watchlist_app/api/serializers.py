import re
from django.db import models
from rest_framework import serializers

from watchlist_app.models import WatchList,SteamPlatform

class SteamPlatformSerializers(serializers.ModelSerializer):
  class Meta:
    model = SteamPlatform
    fields = "__all__"

class WatchListSerializers(serializers.ModelSerializer):
  # len_name = serializers.SerializerMethodField()
  
  class Meta:
    model =  WatchList
    fields = "__all__"


  # def get_len_name(self,object):
  #   return len(object.name)



  # id = serializers.IntegerField(read_only = True)
  # name = serializers.CharField()
  # description = serializers.CharField()
  # active = serializers.BooleanField()


  # def create(self, validated_data):
  #   return WatchList.objects.create(**validated_data)


  # def update(self,instance,validated_data):
  #   instance.name = validated_data.get('name',instance.name)
  #   instance.description = validated_data.get('description',instance.description)
  #   instance.active = validated_data.get('active',instance.active) 
  #   instance.save()
  #   return instance