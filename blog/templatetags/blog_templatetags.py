from django import template
from blog.models import Comment
register = template.Library()


@register.simple_tag
def get_comments_num(id):
    num_comment = Comment.objects.filter(post=id,approved_comment=True).count()
    return num_comment