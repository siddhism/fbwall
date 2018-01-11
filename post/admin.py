from django.contrib import admin
from .models import Post, Like

class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'description']

class LikeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)