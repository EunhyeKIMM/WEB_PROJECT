from django.views.generic import TemplateView, FormView, CreateView, View
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render # 기본 반환값(템플릿 지정하는 함수)
from django.http import HttpResponse, HttpResponseRedirect  # 직접 응답을 만들어서 전달할 때, 이미 만들어진 페이지로 이동
from user.models import User


class Homeview(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        theme = self.request.GET.get('theme')
        if theme : 
            self.request.session['theme']=theme
        return super().get_context_data(**kwargs)

# class SearchFormView(FormView):
#     pass

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    # fields = ['email', 'password', 'age', 'gender', 'phone', 'name']
    template_name = 'registration/register.html'
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

