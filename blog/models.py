from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True, allow_unicode=True)
    Content=models.TextField()
    auther=models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to = "blog/" , blank=True)
    #category
    #tags
    #status
    #published_date

    def __str__(self):
        return self.title

    def snippet(self):
        return self.Content[:100] +"..."
# Create your models here.
