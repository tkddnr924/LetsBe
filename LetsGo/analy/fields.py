from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
from PIL.ExifTags import TAGS

import os


class MyImageFieldFile(ImageFieldFile):
    def save(self, name, content, save=True):
        super(MyImageFieldFile, self).save(name, content, save)

        file_path = self.path
        file_name = file_path.split('/')[-1]
        file_extension = file_name.split('.')[-1]

        print("+++++++++++++++++++++++++++++++++")
        print("open path : " + file_path)
        print("Image FILE Name : " + file_name)
        print("Image FILE extension : " + file_extension)
        print("+++++++++++++++++++++++++++++++++")

        # PILLOW...

        if (file_extension == 'jpg') \
                | (file_extension == 'JPG') \
                | (file_extension == 'jpeg') \
                | (file_extension == 'JPEG'):
            try:
                img = Image.open(file_path)
                info = img._getexif()
                exif = {}
                for tag, value in info.items():
                    decoded = TAGS.get(tag, tag)
                    exif[decoded] = value

            except:
                print("this picture does not have Exif data")
                pass


class MyImageField(ImageField):
    attr_class = MyImageFieldFile

    def __init__(self, *args, **kwargs):
        super(MyImageField, self).__init__(*args, **kwargs)