from django.contrib import admin
from django.db import models


# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=50)
    PassWord = models.CharField(max_length=50)
    User_Mail = models.CharField(max_length=250)
    
    def __unicode__(self):
        return self.UserName
    

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'UserName', 'PassWord', 'User_Mail')

admin.site.register(User, UserAdmin)
