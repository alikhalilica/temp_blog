from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class account (models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length = 200)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    bio = models.TextField()
    avatar = models.ImageField(blank = True , null = True)

    def __str__(self):
        return  "{} - {}".format(self.user.username ,self.user.email)