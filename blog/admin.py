from django.contrib import admin
from .models import Post,Category
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','auther','created_date','get_category']
    list_filter = ("auther", 'created_date','category')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    def get_category(self, obj):
        return "\n".join([p.name for p in obj.category.all()])

admin.site.register(Post,PostAdmin)
admin.site.register(Category)

# Register your models here.
