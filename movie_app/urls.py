from django.urls import path

from .api.v1.views.movies import movie_list, movie_detail, watch_list,watchlist_detail,stream_platform_list,stream_platform_detail

urlpatterns = [
    ##for function based views
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>/', movie_detail, name='movie_detail'),

    ##for class based views
    path('list/', movie_list.as_view(), name='movie_list'),
    path('<int:pk>/', movie_detail.as_view(), name='movie_detail'),

    ##form class based StreamPlatform and WatchList views
    path('watchlist/', watch_list.as_view(), name='watch_list'),
    path('watchlist/<int:pk>/', watchlist_detail.as_view(), name='watchlist_detail'),

    path('stream_platform/', stream_platform_list.as_view(), name='stream_platform_list'),
    path('stream_platform/<int:pk>/', stream_platform_detail.as_view(), name='stream_platform_detail'),

]

