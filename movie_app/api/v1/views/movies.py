from http.client import responses

from django.core.serializers import serialize
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from movie_app.api.v1.serializers.movies import MovieSerializer
from movie_app.models import Movie



# Create your views here.

"""to create API only using Django"""

# def movie_list(request):
#     movies=Movie.objects.all()
#     data=list(movies.values())
#     return JsonResponse(data, safe=False)


# def movie_detail(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
#     data = {
#         "id": movie.id,
#         "name": movie.name,
#         "description": movie.description,
#     }
#     return JsonResponse(data)

"""................................................................................................"""


"""to create API using REST framework, function based view"""

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method=='GET':
        movies = Movie.objects.all()
        serializer=MovieSerializer(movies, many=True)
        return Response (serializer.data)
    if request.method=='POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True})
        else:
            return Response(serializer.errors)




@api_view(['GET','PUT','PATCH','DELETE'])
def movie_detail(request, pk):
    if request.method=='GET':
        movie = get_object_or_404(Movie, pk=pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)

    if request.method=='PUT':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(instance=movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':True})
        else:
            return Response(serializer.errors)

    if request.method == 'PATCH':
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(instance=movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True})
        else:
            return Response(serializer.errors)


    if request.method=='DELETE':
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response({'success':True})

"""................................................................................."""


"""using class based views"""

class movie_list(APIView):
    """
    List all movies or create new movie
    """

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class movie_detail(APIView):
    """
    Retrieve, update or delete a movie instance
    """
    def get_object(selfself, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        movie=self.get_object(pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self,request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        movie=self.get_object(pk)
        movie.delete()
        return Response({'success':True}, status=status.HTTP_204_NO_CONTENT)