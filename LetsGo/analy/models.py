from django.db import models
from django.core.urlresolvers import reverse

from analy.fields import MyImageField

# Create your models here.

"""
model 정리

1. User
    user id
    user name

2. Picture
    user id
    picture id
    picture name
    picture image (field)

3. Exif
    picture id
    exif ...
"""

class User(models.Model):
    name = models.CharField("Nick Name", max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('analy:index', args=(self.id, ))


class Photo(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField("Title", max_length=100)
    image = MyImageField(upload_to='photo/')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

