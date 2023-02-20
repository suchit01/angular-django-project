from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.MoviesView.as_view(), name='MoviesView'),
    path('movies/<int:pk>', views.MoviesDetailView.as_view(), name='SpecificMoviesView'),
    path('actors/', views.ActorsView.as_view(), name='ActorsView'),
]