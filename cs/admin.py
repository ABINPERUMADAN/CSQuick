from django.contrib import admin

# Register your models here.
from . import models

class studentadmin(admin.ModelAdmin):
    search_fields=('username','name')
    list_display=('name','username')

admin.site.register(models.student,studentadmin)

class booksadmin(admin.ModelAdmin):
    list_display=('bookid','bookname','bookauthor','issuedate','renewdate','user','status', )
    search_fields=('bookid','bookname','user__username')
    raw_id_fields = ("user",)

admin.site.register(models.books,booksadmin)

class laptopadmin(admin.ModelAdmin):
    list_display=('lapid','user','datel','status', )
    search_fields=('lapid','user__username',)
    raw_id_fields = ('user',)

admin.site.register(models.laptop,laptopadmin)

# class studentlibraryadmin(admin.ModelAdmin):
#     list_display=('sbookid','suser','issuedate','returndate','sStatus',)
#     search_fields=('suser__username','sbookid__bookid',)
#     raw_id_fields=('sbookid','suser',)
# admin.site.register(models.studentlibrary,studentlibraryadmin)

# class stafflibraryadmin(admin.ModelAdmin):
#     list_display=('stbookid','stuser','issuedate','returndate','stStatus',)
#     search_fields=('stuser__username','stbookid__bookid',)
#     raw_id_fields=('stbookid','stuser',)
# admin.site.register(models.stafflibrary,stafflibraryadmin)

class staffadmin(admin.ModelAdmin):
    search_fields=('username','name')
    list_display=('name','username')

admin.site.register(models.staff,staffadmin)

class eventadmin(admin.ModelAdmin):
    search_fields=('programme','by',)
    list_display=('programme','link','by','event_date')

admin.site.register(models.events,eventadmin)