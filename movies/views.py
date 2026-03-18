from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer


@api_view(['GET'])
def movie_list(request):
    language = request.GET.get('language')

    if language:
        movies = Movie.objects.filter(language__iexact=language)
    else:
        movies = Movie.objects.all()

    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)