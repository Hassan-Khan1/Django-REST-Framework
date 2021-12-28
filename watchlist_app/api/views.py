import re
from rest_framework import serializers
from watchlist_app.models import *
from watchlist_app.api.serializers import MovieSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def movie_list(request):
  movie = Movie.objects.all()

  serializer = MovieSerializers(movie,many = True)

  return Response(serializer.data )

@api_view()
def movie_details(request,pk):
  movie = Movie.objects.get(pk=pk)

  serializer = MovieSerializers(movie)
  return Response(serializer.data)