from django.db import models

# Create your models here.
class Instagram(models.Model):
    post_desc = models.CharField(max_length=500)

class Comment(models.Model):
    post = models.ForeignKey(Instagram, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)




