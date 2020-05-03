from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','auther','created_date']
    list_filter = ("auther", 'created_date')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post,PostAdmin)

# Register your models here.
