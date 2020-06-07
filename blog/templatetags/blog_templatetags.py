from django import template
from blog.models import Comment,Category,Post
register = template.Library()


@register.simple_tag
def get_comments_num(id):
    num_comment = Comment.objects.filter(post=id,approved_comment=True).count()
    return num_comment


@register.inclusion_tag("blog/blog-categories.html")
def show_categories():
    # 1 - gather all the data we need
    categories = Category.objects.all()
    posts = Post.objects.filter(status=1)
    # 2 - get the right posts by filtering with category name
    context ={}
    for category in categories:
        #print(category.name)
        counted = posts.filter(category__name =category.name).count()
        context[category.name]=counted
        #{'programing': 1, 'bride': 2, 'wedding': 1}
    return {"categories":context}


@register.inclusion_tag("blog/blog-populorpost.html")
def show_populorpost(count=2):
    posts = Post.objects.filter(status=1)[:count]
    return {"posts":posts}

'''
list = ["ali","hassan","hossein"]
list[:2] # n : m-1
'''