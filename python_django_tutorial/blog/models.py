from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Cada classe é uma tabela na base de dados


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
