from django.views.generic import ListView, DetailView
from analy.models import User, Photo
from analy.forms import SearchUserForm
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

from django.db.models import Q
from django.shortcuts import render, HttpResponse
import json
from django.core.urlresolvers import reverse
import pdb
# Create your views here.


class UserDV(DetailView):
    model = User
    template_name = 'analy/analy_result.html'


class PictureDV(DetailView):
    model = User
    template_name = 'analy/analy_picture_list.html'

    def get_context_data(self, **kwargs):
        context = super(PictureDV, self).get_context_data(**kwargs)
        photo_list = context['object'].photo_set.all()
        paginator = Paginator(photo_list, 12)

        page = self.request.GET.get('page')

        try:
            photo_data = paginator.page(page)
        except PageNotAnInteger:
            photo_data = paginator.page(1)
        except EmptyPage:
            photo_data = paginator.page(paginator.num_pages)

        context['photo_data'] = photo_data
        return context


class UserLV(ListView):
    model = User
    template_name = 'analy/analy_another_user.html'

    def post(self, request, *args, **kwargs):
        form = SearchUserForm(request.POST)
        search_user = '%s' % request.POST['search_word']

        user_list = User.objects.filter(Q(name__icontains=search_user)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = search_user
        context['my_list'] = user_list

        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        flag = request.path.split('/')[-1]

        if flag == 'another_user':
            return super(UserLV, self).get(request, args, kwargs)
        else:
            context = {}
            context['object'] = User.objects.filter(id=flag).first()
            photo_list = context['object'].photo_set.all()
            paginator = Paginator(photo_list, 12)
            page = self.request.GET.get('page')

            try:
                photo_data = paginator.page(page)
            except PageNotAnInteger:
                photo_data = paginator.page(1)
            except EmptyPage:
                photo_data = paginator.page(paginator.num_pages)

            context['photo_data'] = photo_data

            return render(request, 'analy/another_user_list.html', context)


class AnotherUserDV(DetailView):
    model = User
    template_name = 'analy/another_user_list.html'


# GET JSON 필요

def get_exif_json(request, pk):
    """ /json/data/photo_id """
    user_id = request.path.split('/')[-1]
    user_data = User.objects.filter(id=user_id).first()
    photo_data = user_data.photo_set.all()
    data = []
    for photo in photo_data:
        exif_data = photo.exif_set.all().first().dic()
        data.append(exif_data)

    return HttpResponse(json.dumps(data), content_type='application/json')


def get_photo_json(request, pk):
    photo_id = request.path.split('/')[-1]
    photo_data = Photo.objects.filter(id=photo_id).first()
    data = photo_data.dic()

    return HttpResponse(json.dumps(data), content_type='application/json')
