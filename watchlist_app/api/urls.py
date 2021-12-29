


from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import (ReviewCreate, WatchListAV,WatchDetailsAV,SteamPlatformAV,
                                    StreamPlatFormDetailAV,ReviewList,ReviewDetial,
                                    ReviewCreate,StreamPlatformAS
                                    )
router = DefaultRouter()
router.register('stream',StreamPlatformAS,basename= 'streamplatform')

urlpatterns = [

    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie_details'),


# Routers
    path('',include(router.urls)),
    # path('steam/', SteamPlatformAV.as_view(), name='steam'),
    # path('steam/<int:pk>', StreamPlatFormDetailAV.as_view(), name='steam-detials'),

# Generic Views

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/', ReviewDetial.as_view(), name='review-details'),

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetial.as_view(), name='review-details'),

]
