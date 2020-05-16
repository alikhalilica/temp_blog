from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.contrib import messages
from .models import Post,Category
from taggit.models import Tag
from account.models import account
# root page
def index(request):
    users = account.objects.all()
    user = get_object_or_404(users,user__username = "alikhalili")
    #posts= Post.objects.all().order_by("-created_date")
    posts = Post.objects.filter(status=1).order_by("-created_date")
    context = {"posts":posts,"writer":user}
    return render(request,"blog/blog-home.html",context)
# Create your views here.
def post_view(request,post_slug):
    users = account.objects.all()
    user = get_object_or_404(users,user__username = "alikhalili")
    posts = Post.objects.all().order_by("-created_date")
    post = get_object_or_404(posts,slug=post_slug)
    category = Category.objects.all()
    context = {"post":post,"categories":category, "writer":user}
    return render(request,"blog/blog-single.html",context)