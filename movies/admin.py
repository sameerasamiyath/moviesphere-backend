from django.contrib import admin
from .models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'release_year', 'is_premium')
    list_filter = ('language', 'is_premium', 'genre')
    search_fields = ('title', 'language')
    ordering = ('language', 'title')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)