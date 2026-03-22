from django.urls import path
from .views import movie_list   # 👈 small m

urlpatterns = [
    path('movies/', movie_list),
]