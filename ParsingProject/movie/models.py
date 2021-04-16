from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='media')
    genre = models.CharField(max_length=30)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.name

