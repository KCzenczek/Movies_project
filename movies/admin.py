from django.contrib import admin
from movies.models import Person, Movie, Role


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role']