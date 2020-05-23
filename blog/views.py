from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.contrib import messages
from .models import Post,Category,Comment
from taggit.models import Tag
from account.models import account
from .forms import CommentForm


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
    #post = Post.objects.get(slug=post_slug)
    comments = Comment.objects.filter(post = post,approved_comment=True,parent__isnull=True)
    if (request.method == 'POST'):
        form = CommentForm(data=request.POST) #**kwarg *arg
        if form.is_valid():
            parent_obj = None

            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)

                if parent_obj:
                    reply_comment = form.save(commit=False)
                    reply_comment.parent = parent_obj

            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            #print(form.cleaned_data)
            form.save()
            #return HttpResponse("contact saved")
            messages.success(request,'your comment have been recieved')
            return HttpResponseRedirect(request.path_info) #path_info == url client 
    else:
        
        category = Category.objects.all()
        form = CommentForm()
        context = {"post":post,"categories":category, "writer":user , "comments":comments,"form":form}
        return render(request,"blog/blog-single.html",context)