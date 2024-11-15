from django.contrib import admin
from .models import *
# Register your models here.

# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id','title','body','date','author')

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Region)