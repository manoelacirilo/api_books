from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=150)
    synopsis = models.TextField()
    genre = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    restricted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.author.name} - {self.year}'
