


from django.contrib import admin
from django.urls import path,include

from watchlist_app.api.views import (WatchListAV,WatchDetailsAV,SteamPlatformAV,
                                    StreamPlatFormDetailAV,ReviewList,ReviewDetial,
                                    )


urlpatterns = [

    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie_details'),
    path('steam/', SteamPlatformAV.as_view(), name='steam'),
    path('steam/<int:pk>', StreamPlatFormDetailAV.as_view(), name='steam-detials'),

# Generic Views

    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetial.as_view(), name='review-details'),

]
