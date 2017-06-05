from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

    # 여기서 user랑 photo 데이터 받음
