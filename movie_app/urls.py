from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .api.v1.views.movies import movie_list, movie_detail, watch_list, watchlist_detail, stream_platform_list, \
    stream_platform_detail, WatchlistCRUDView, WatchlistView, WatchListDetailView, WatchListRetrieveUpdateDeleteView, \
    WatchListUpdateView, NetflixWatchListView, WatchlistViewSet,StreamPlatformViewSet

# urlpatterns = [
#     ##for function based views
#     # path('list/', movie_list, name='movie_list'),
#     # path('<int:pk>/', movie_detail, name='movie_detail'),
#
#     ##for class based views
#     path('list/', movie_list.as_view(), name='movie_list'),
#     path('<int:pk>/', movie_detail.as_view(), name='movie_detail'),
#
#     ##form class based StreamPlatform and WatchList views
#     # path('watchlist/', watch_list.as_view(), name='watch_list'),
#     # path('watchlist/<int:pk>/', watchlist_detail.as_view(), name='watchlist_detail'),
#
#     path('stream_platform/', stream_platform_list.as_view(), name='stream_platform_list'),
#     path('stream_platform/<int:pk>/', stream_platform_detail.as_view(), name='stream_platform_detail'),
#
#     ##for GenericListView and mixins
#     # path('watchlist/', WatchlistCRUDView.as_view(), name='watch_list'),
#     # path('watchlist/<int:pk>/', WatchlistCRUDView.as_view(), name='watch_detail'),
#
#     ##for Concrete API view
#     path('watchlist/', WatchlistView.as_view(), name='watch_list'),
#     # path('watchlist/<int:pk>/', WatchListUpdateView.as_view(), name='watch_detail'),
#     path('watchlist/<int:pk>/', WatchListRetrieveUpdateDeleteView.as_view(), name='watch_detail'),
#
#     #for listview with netflix shows only
#     path('watchlistNetflix/', NetflixWatchListView.as_view(), name='watch_list_netflix'),
#
# ]

router = DefaultRouter()
router.register(r'watchlist', WatchlistViewSet, basename='watchlist')
router.register(r'stream_platform', StreamPlatformViewSet, basename='platforms')

urlpatterns = [
    path('', include(router.urls)),
]
