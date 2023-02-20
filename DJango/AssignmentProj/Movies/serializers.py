from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import MoviesList, ActorsList


class MoviesListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MoviesList
        fields = ['id', 'title', 'desc', 'release_date', 'num_actors', 'upvotes', 'downvotes']


class ActorsListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActorsList
        fields = ['name', 'dob', 'num_movies']