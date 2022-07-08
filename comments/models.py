from django.db import models

from core.models import Book
from users.models import User


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'User: {self.user.name}, Comment: {self.comments}, Book: {self.book.title}'
