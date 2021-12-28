import re
from rest_framework import HTTP_HEADER_ENCODING, serializers
from watchlist_app.models import *
from watchlist_app.api.serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def movie_list(request):
  if request.method == "GET":
    movie = Movie.objects.all()
    serializer = MovieSerializers(movie,many = True)
    return Response(serializer.data )

  if request.method == "POST":
    serializer = MovieSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)
      

@api_view(['GET','PUT','DELETE'])
def movie_details(request,pk):
  if request.method == 'GET':
    
    try:
      movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
      return Response({'Error': 'Movie not Found'},status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializers(movie)
    return Response(serializer.data)
  
  if request.method == "PUT":
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializers(movie,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


  if request.method == "DELETE":
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
