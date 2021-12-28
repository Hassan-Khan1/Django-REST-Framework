


from django.contrib import admin
from django.urls import path,include

from watchlist_app.api.views import WatchListAV,WatchDetailsAV,SteamPlatformAV

urlpatterns = [


    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie_details'),
    path('steam/', SteamPlatformAV.as_view(), name='steam'),


]
