from django.contrib import admin
from django.db import models


# Create your models here.
######博客内容######
class BlogPost(models.Model):
    blog_type_id = models.IntegerField()
    title = models.CharField(max_length=150)
    content = models.TextField()
    time_stamp = models.DateTimeField()
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_type_id', 'title', 'content', 'time_stamp')
    
######博客回复######
class BlogReply(models.Model):
    content_id = models.IntegerField()
    re_id = models.IntegerField(null=True)
    re_text = models.CharField(max_length=600)
    re_time = models.DateTimeField()
    re_user = models.CharField(max_length=20)
    
class BlogReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'content_id', 're_id', 're_text', 're_user', 're_time', 're_user')
    
######博客分类######
class BlogType(models.Model):
    type_name = models.CharField(max_length=20)
    
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')

######绑定管理######
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogReply, BlogReplyAdmin)
admin.site.register(BlogType, BlogTypeAdmin)





