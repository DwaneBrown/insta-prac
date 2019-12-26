from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime as dt
from django.utils import timezone


class Location(models.Model):
    area = models.CharField(max_length=30)

    def __str__(self):
        return self.area

    class Meta:
        ordering = ["area"]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
