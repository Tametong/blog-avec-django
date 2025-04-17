from django.contrib import admin
from posts.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'last_update', 'created_on', 'published', 'content',)
    list_editable = ('published',)

admin.site.register(BlogPost, BlogPostAdmin)
# Register your models here.
