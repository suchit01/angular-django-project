from .models import MoviesList, ActorsList
from .serializers import MoviesListSerializer, ActorsListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
class MoviesView(APIView):
    allowed_methods = ['GET']
    serializer_class = MoviesListSerializer

    def get(self, request, *args, **kwargs):
        queryset = MoviesList.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class MoviesDetailView(APIView):
    allowed_methods = ['GET', 'PUT']

    def get(self, request, pk, *args, **kwargs):
        queryset = MoviesList.objects.filter(id=pk)
        movie = get_object_or_404(queryset)
        serializer = MoviesListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = MoviesList.objects.filter(id=pk)
        movie = get_object_or_404(queryset)
        data = request.data
        if 'is_upvote' in data and data['is_upvote']:
            movie.upvote()
        elif 'is_downvote' in data and data['is_downvote']:
            movie.downvote()
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = MoviesListSerializer(movie)
        return Response(serializer.data)


class ActorsView(APIView):
    allowed_methods = ['GET']
    serializer_class = ActorsListSerializer

    def get(self, request, *args, **kwargs):
        queryset = ActorsList.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)