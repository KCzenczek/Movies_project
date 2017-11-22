from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Movie(models.Model):
    title = models.CharField(max_length=24)
    description = models.TextField()
    director = models.ForeignKey(
        Person,
        related_name='movie_person_director',
        on_delete=models.CASCADE,
    )
    actors = models.ManyToManyField(
        Person,
        related_name='movie_person_actors',
        through='Role',
    )
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Role(models.Model):
    role = models.CharField(max_length=24)
    person = models.ForeignKey(
        Person,
        related_name='role_person',
        on_delete=models.CASCADE,
    )
    movie = models.ForeignKey(
        Movie,
        related_name='role_movie',
        on_delete=models.CASCADE,
    )
