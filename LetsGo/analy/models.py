from django.db import models
from django.core.urlresolvers import reverse

from analy.fields import MyImageField

import pdb
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
        return reverse('analy:another', args=(self.id, ))


class Photo(models.Model):

    def file_path(instance, filename):

        return '/'.join(filter(None, (str(instance.user_id), filename)))

    user = models.ForeignKey(User)
    title = models.CharField("Title", max_length=100)
    image = MyImageField(upload_to=file_path)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title



class Exif(models.Model):
    photo = models.ForeignKey(Photo)
    make = models.CharField("Manufacturer", max_length=50)
    camera_model = models.CharField("Model", max_length=50)
    date_time = models.CharField("Date Time", max_length=50)
    iso_speed = models.CharField("ISO Speed", max_length=50)
    color = models.CharField("Color Space", max_length=50)
    latitude = models.CharField("Latitude", max_length=50)
    longitude = models.CharField("Longitude", max_length=50)
    orientation = models.CharField("Direction of Rotation", max_length=50)
    focal_length = models.CharField("Focus Length", max_length=50)
    flash = models.CharField("Flash", max_length=50)

    class Meta:
        db_table = 'Exif_info'
        ordering = ('-date_time', )


    def __str__(self):
        return self.make + "/" + self.latitude + '/' + self.longitude

    def dic(self):
        fields = [
            'make', 'camera_model', 'date_time', 'iso_speed', 'color',
            'latitude', 'longitude', 'orientation', 'focal_length', 'flash'
        ]

        result = {}

        for field in fields:
            result[field] = self.__dict__[field]

        return result