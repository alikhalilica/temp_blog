from django.contrib import admin
from .models import Post,Category,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','auther','created_date','get_category']
    list_filter = ("auther", 'created_date','category')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    def get_category(self, obj):
        return "\n".join([p.name for p in obj.category.all()])

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','subject','email']
    search_fields = ['name', 'subject','body']
    


admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)

# Register your models here.
