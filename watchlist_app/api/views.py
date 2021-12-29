import re
from rest_framework import HTTP_HEADER_ENCODING, serializers, views
from watchlist_app.models import Review, WatchList,SteamPlatform
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from watchlist_app.api.serializers import (ReviewSerializers, WatchListSerializers,
                                           SteamPlatformSerializers)

class ReviewDetial(mixins.RetrieveModelMixin, generics.GenericAPIView):
  queryset =  Review.objects.all()
  serializer_class = ReviewSerializers
  
  def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)


class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset =  Review.objects.all()
    serializer_class = ReviewSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SteamPlatformAV(APIView):

  def get(self,request):
    platform = SteamPlatform.objects.all()
    serializer = SteamPlatformSerializers(platform,many = True)
    return Response(serializer.data)

  def post(self,request):
    serializer = SteamPlatformSerializers(data= request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)



class StreamPlatFormDetailAV(APIView):

  def get(self,request,pk):
    try:
      platform = SteamPlatform.objects.get(pk=pk)
    except SteamPlatform.DoesNotExist:
      return Response({'Error': 'Movie not Found'},status=status.HTTP_404_NOT_FOUND)
    serializer = SteamPlatformSerializers(platform)
    return Response(serializer.data)

  def put(self,request,pk):
    platform = SteamPlatform.objects.get(pk=pk)
    serializer = SteamPlatformSerializers(platform,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk):
    platform = SteamPlatform.objects.get(pk=pk)
    platform.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class WatchListAV(APIView):

  def get(self,request):
    movies = WatchList.objects.all()
    serializer = WatchListSerializers(movies, many=True)
    return Response(serializer.data)

  def post(self,request):
    serializer = WatchListSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)

class WatchDetailsAV(APIView):

  def get(self,request,pk):
    try:
      movie = WatchList.objects.get(pk=pk)
    except WatchList.DoesNotExist:
      return Response({'Error': 'Not Found'},status=status.HTTP_404_NOT_FOUND)
    serializer = WatchListSerializers(movie)
    return Response(serializer.data)


  def put(self,request,pk):
    movie = WatchList.objects.get(pk=pk)
    serializer = WatchListSerializers(movie,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk):
    movie = WatchList.objects.get(pk=pk)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def movie_list(request):
#   if request.method == "GET":
#     movie = Movie.objects.all()
#     serializer = MovieSerializers(movie,many = True)
#     return Response(serializer.data )

#   if request.method == "POST":
#     serializer = MovieSerializers(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors)
      

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#   if request.method == 'GET':
    
#     try:
#       movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#       return Response({'Error': 'Movie not Found'},status=status.HTTP_404_NOT_FOUND)
#     serializer = MovieSerializers(movie)
#     return Response(serializer.data)
  
#   if request.method == "PUT":
#     movie = Movie.objects.get(pk=pk)
#     serializer = MovieSerializers(movie,data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#   if request.method == "DELETE":
#     movie = Movie.objects.get(pk=pk)
#     movie.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
