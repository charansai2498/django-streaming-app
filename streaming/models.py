from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    release_date=models.DateField()
    rating=models.DecimalField(max_digits=3,decimal_places=1)
    poster=models.ImageField(upload_to='posters/',blank=True,null=True)
    video=models.FileField(upload_to='movies/',blank=True,null=True)
    def __str__(self):
        return self.title
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    favorite_movies=models.ManyToManyField(Movie,blank=True)
    def __str__(self):
        return f"{self.user.username}'s profile "