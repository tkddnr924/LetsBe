from django.views.generic import TemplateView
from analy.forms import PhotoForm
from analy.models import User, Photo, Exif
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from PIL import Image
from PIL.ExifTags import TAGS
from analy.core import core



class HomeView(TemplateView):
    template_name = 'home.html'
    # 여기서 user 랑 photo 데이터 받음

    def post(self, request, *args, **kwargs):
        md_user = User()
        form = PhotoForm(request.POST, request.FILES)

        # --- Checking Form
        if form.is_valid():
            md_user.name = form.cleaned_data['user']
            md_user.save()
            files = form.files.getlist('image')

            # --- save photo file
            for photo in files:
                md_photo = Photo(user=md_user, image=photo, title=photo.__str__())
                md_photo.save()

                # --- PILLOw
                file_extension = photo.__str__().split('.')[-1]
                file_path = md_photo.image.path

                # --- jpg checking
                if (file_extension == 'jpg') \
                        | (file_extension == 'JPG') \
                        | (file_extension == 'jpeg') \
                        | (file_extension == 'JPEG'):
                    try:
                        # --- to extract exif
                        img = Image.open(file_path)
                        info = img._getexif()
                        exif = {}

                        for tag, value in info.items():
                            decoded = TAGS.get(tag, tag)
                            exif[decoded] = value

                        # --- calculate exif
                        exif_info = core.ExifInfo(exif)
                        exif_info.calculate_all()

                        # --- save exif model
                        md_exif = Exif(photo=md_photo)
                        md_exif.make = exif_info.make
                        md_exif.camera_model = exif_info.model
                        md_exif.color = exif_info.color_space
                        md_exif.date_time = exif_info.date_time
                        md_exif.iso_speed = exif_info.iso_speed
                        md_exif.latitude = exif_info.lat
                        md_exif.longitude = exif_info.lng
                        md_exif.orientation = exif_info.orientation
                        md_exif.focal_length = exif_info.focal_length
                        md_exif.flash = exif_info.flash

                        md_exif.save()

                    except:
                        print("this picture does not have Exif data")
                        pass


        return redirect(reverse('analy:index', args=(md_user.id, )))