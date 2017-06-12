from django.views.generic import ListView, DetailView
from analy.models import User
from analy.forms import SearchUserForm
from django.db.models import Q
from django.shortcuts import render
from django.core.urlresolvers import reverse
import pdb
# Create your views here.

class UserDV(DetailView):
    model = User
    template_name = 'analy/analy_result.html'

class PictureDV(DetailView):
    model = User
    template_name = 'analy/analy_picture_list.html'


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
        print("flag is " + flag)
        if flag == 'another_user':
            return super(UserLV, self).get(request, args, kwargs)
        else:
            context = {}
            context['object'] = User.objects.filter(id=flag).first
            return render(request, 'analy/another_user_list.html', context)



class AnotherUserDV(DetailView):
    model = User
    template_name = 'analy/another_user_list.html'


# GET JSON 필요
