from django.contrib import admin
from .models import Movie, UserProfile
# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display=('title','release_date')