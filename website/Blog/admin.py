from django.contrib import admin
from .models import Category,Tag,BlogPost,PostCommet
from  django.contrib.admin.options import ModelAdmin


class CategoryAdmin(ModelAdmin):
    list_display = ['cat_name','created_date']
    search_fields = ['cat_name']
    list_filter = ["created_date"] 
admin.site.register(Category,CategoryAdmin)

class TagAdmin(ModelAdmin):
    list_display = ['tag_name','created_date']
    search_fields = ['tag_name']
    list_filter = ["created_date"] 
admin.site.register(Tag,TagAdmin)

class BlogPostAdmin(ModelAdmin):
    list_display = ['title','post_cat','post_tag','uploaded_by']
    search_fields = ['title']
    list_filter = ['created_date','post_cat','post_tag'] 
admin.site.register(BlogPost,BlogPostAdmin)

class PostCommetAdmin(ModelAdmin):
    list_display = ["post","msg","pub_date"]
    search_fields = ["post","msg","commited_by"]
    list_filter = ["pub_date","flag"]    
admin.site.register(PostCommet, PostCommetAdmin)

