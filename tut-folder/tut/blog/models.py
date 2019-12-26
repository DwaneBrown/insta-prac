from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import datetime as dt


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ["first_name"]


class Location(models.Model):
    area = models.CharField(max_length=30)

    def __str__(self):
        return self.area

    class Meta:
        ordering = ["area"]


class Pics(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_posted =  models.DateTimeField(default=timezone.now)
    image = models.ImageField(default="default.jpg", upload_to="images/")

    def __str__(self):
        return self.title

    def save_pics(self):
        self.save()

    def get_absolute_url(self):
        return reverse('pics-detail', kwargs={'pk': self.pk})


    @classmethod
    def todays_pics(cls):
        today = dt.date.today()
        pics = cls.objects.all()
        return pics

    @classmethod
    def days_pics(cls, date):
        pics = cls.objects.filter(date_posted__date=date)
        return pics

    @classmethod
    def search_by_category(cls, search_term):
        pics = cls.objects.filter(category__choise__icontains=search_term)
        return pics
