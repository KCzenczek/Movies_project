from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MoviesView(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(
            movies,
            many=True,
            context={
                "request": request,
            }
        )
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class MovieView(APIView):
    def get_object(self, id):
        try:
            return Movie.objects.get(pk=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(
            movie,
            context={
                "reguest": request,
            }
        )
        return Response(serializer.data)

    def delete(self, reguest, id, format=None):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(
            movie,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
