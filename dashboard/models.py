from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 300)
    author = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    boughtBool = models.BooleanField(default='False')
    image = models.ImageField()
    price = models.CharField(max_length = 20)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    def __str__(self):
        return self.title
