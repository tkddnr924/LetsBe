from django.views.generic import TemplateView
from analy.forms import PhotoForm
from analy.models import User, Photo
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
import pdb


class HomeView(TemplateView):
    template_name = 'home.html'
    # 여기서 user랑 photo 데이터 받음

    def post(self, request, *args, **kwargs):
        md_user = User()
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            md_user.name = form.cleaned_data['user']
            md_user.save()
            files = form.files.getlist('image')

            for photo in files:
                md_photo = Photo(user=md_user, image=photo, title=photo.__str__())
                md_photo.save()

        return redirect(reverse('analy:index', args=(md_user.id, )))