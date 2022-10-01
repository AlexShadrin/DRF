from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return self.last_name

class Biographies(models.Model):
    text = models.TextField(blank=True, null=True)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

class Book(models.Model):
    name = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)