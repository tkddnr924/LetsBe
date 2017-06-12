from django.contrib import admin
from analy.models import User, Photo, Exif

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

class ExifAdmin(admin.ModelAdmin):
    list_display = ('make', )


admin.site.register(User, UserAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Exif, ExifAdmin)