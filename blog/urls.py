from . import views
from django.urls import path

app_name = "blog"

urlpatterns = [
    path('',views.index,name='index'), # {% url 'website:index' %}
    path('post/<str:post_slug>',views.post_view,name='post'), # {% url 'blog:post' %}
]

#/blog/post/ajsdhasjfd