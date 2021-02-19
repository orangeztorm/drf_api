from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

# Create your models here.

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
