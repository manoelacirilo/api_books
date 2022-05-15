from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    restricted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.author} - {self.year}'
