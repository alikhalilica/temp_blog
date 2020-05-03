from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.contrib import messages
from .models import Post
# root page
def index(request):
    posts= Post.objects.all().order_by("-created_date")
    context = {"posts":posts}
    return render(request,"blog/blog-home.html",context)
# Create your views here.
def post_view(request,post_slug):
    posts= Post.objects.all().order_by("-created_date")
    post = get_object_or_404(posts,slug=post_slug)
    context = {"post":post}
    return render(request,"blog/blog-single.html",context)