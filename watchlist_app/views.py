from django.shortcuts import render

# Create your views here.
from watchlist_app.models import *
from django.http import JsonResponse

def movie_list(request):
  movies = WatchList.objects.all()

  data = {
    'movies': list(movies.values())
  }
  # print(movies.values())
  return JsonResponse(data)


def movie_detials(request,pk):
  movie = WatchList.objects.get(pk=pk)
  data = {
    'name':movie.name,
    'description' : movie.description,
    'active' : movie.active
  }

  return JsonResponse(data)