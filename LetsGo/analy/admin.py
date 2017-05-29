from django.contrib import admin
from analy.models import User, Photo

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


admin.site.register(User, UserAdmin)
admin.site.register(Photo, PhotoAdmin)