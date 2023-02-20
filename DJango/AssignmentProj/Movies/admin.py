from django.contrib import admin

# Register your models here.

from .models import MoviesList, ActorsList

admin.site.register(MoviesList)
admin.site.register(ActorsList)