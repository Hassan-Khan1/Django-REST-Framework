import re
from django.db import models
from django.db.models import fields
from rest_framework import serializers

from watchlist_app.models import Review, WatchList,SteamPlatform


class ReviewSerializers(serializers.ModelSerializer):
  review_user = serializers.StringRelatedField(read_only=True)
  class Meta:  
    model = Review
    # fields = "__all__"
    exclude= ('watchlist',)

class WatchListSerializers(serializers.ModelSerializer):
  # len_name = serializers.SerializerMethodField()
  reviews = ReviewSerializers(many=True,read_only=True)

  class Meta:
    model =  WatchList
    fields = "__all__"

class SteamPlatformSerializers(serializers.ModelSerializer):

  watchlist = WatchListSerializers(many=True,read_only= True)

  class Meta:
    model = SteamPlatform
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