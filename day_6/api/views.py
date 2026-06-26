from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie
from .serializers import MovieSerializer

# 1. LIST (Get all) & CREATE (Post new)
@api_view(['GET', 'POST'])
def movie_list_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. RETRIEVE (Get one), UPDATE (PUT/PATCH), & DELETE
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def movie_detail(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

    # GET: Retrieve a single movie
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    # PUT: Full Update (requires all fields)
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PATCH: Partial Update (updates only passed fields)
    elif request.method == 'PATCH':
        serializer = MovieSerializer(movie, data=request.data, partial=True) # <--- partial=True handles this!
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE: Remove the movie
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)