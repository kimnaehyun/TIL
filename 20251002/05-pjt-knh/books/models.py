from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    explanation = models.TextField()
    review_rating = models.IntegerField()
    author = models.CharField()