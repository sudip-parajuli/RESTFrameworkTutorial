from django.urls import path

from .api.v1.views.movies import movie_list, movie_detail

urlpatterns = [
    ##for function based views
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>/', movie_detail, name='movie_detail'),

    ##for class based views
    path('list/', movie_list.as_view(), name='movie_list'),
    path('<int:pk>/', movie_detail.as_view(), name='movie_detail'),
]

