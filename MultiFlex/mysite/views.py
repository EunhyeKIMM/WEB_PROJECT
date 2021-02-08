from django.views.generic import TemplateView, FormView, CreateView, View
from django.urls import reverse_lazy
from django.shortcuts import render # 기본 반환값(템플릿 지정하는 함수)
from django.http import HttpResponse, HttpResponseRedirect  # 직접 응답을 만들어서 전달할 때, 이미 만들어진 페이지로 이동
from user.models import User
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import AccessMixin

class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object."

    def get(self, request, *args, **kwargs):
        self.object = self.get_object() # 모델 인스턴스 얻기
        if self.request.user != self.object.user_id:  # 소유자인지 확인
            self.handle_no_permission()     # 예외 발생

        return super().get(request, *args, **kwargs)

class Homeview(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        theme = self.request.GET.get('theme')
        if theme : 
            self.request.session['theme']=theme
        return super().get_context_data(**kwargs)

class SearchFormView(FormView):
    pass

