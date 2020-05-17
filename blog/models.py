from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = ((0,"draft"),(1,"publish"))
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True, allow_unicode=True)
    Content=models.TextField()
    auther=models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to = "blog/" , blank=True)
    #category=models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True) #{{post.category.name}}
    category=models.ManyToManyField(Category) #{% for  cat in post.category.all %} <li><a href="#">{{cat.name}}</a></li> {% endfor %}
    tags = TaggableManager()
    status = models.IntegerField(choices = STATUS,default=0 )
    updated_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank =True,null = True)
    #published_date
    def __str__(self):
        return self.title

    def snippet(self):
        return self.Content[:100] +"..."


class Comment (models.Model):
    name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 200)
    email = models.EmailField()
    body = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True,blank=True, null=True)

    def __str__ (self):
        return self.subject

    

# Create your models here.
#django-taggit