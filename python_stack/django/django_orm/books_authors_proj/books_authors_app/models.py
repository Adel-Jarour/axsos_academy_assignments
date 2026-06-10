from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    notes = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    author = models.ManyToManyField(Author, related_name='books')