from .models import Movie, Person, Role
from rest_framework import serializers


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = PersonSerializer(read_only=True)
    actors = PersonSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'director', 'actors', 'year']


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    person = PersonSerializer()
    movie = MovieSerializer()

    class Meta:
        model = Role
        fields = ['role', 'person', 'movie']
