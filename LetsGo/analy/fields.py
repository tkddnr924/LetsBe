from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
from PIL.ExifTags import TAGS


class MyImageFieldFile(ImageFieldFile):
    def save(self, name, content, save=True):
        super(MyImageFieldFile, self).save(name, content, save)

class MyImageField(ImageField):
    attr_class = MyImageFieldFile

    def __init__(self, *args, **kwargs):
        super(MyImageField, self).__init__(*args, **kwargs)