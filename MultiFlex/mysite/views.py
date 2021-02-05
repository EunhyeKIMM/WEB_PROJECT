from django.views.generic import TemplateView, FormView, CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from user.models import User


class Homeview(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        theme = self.request.GET.get('theme')
        if theme : 
            self.request.session['theme']=theme
        return super().get_context_data(**kwargs)

# class Homeview(TemplateView):
#     template_name = 'registration/login.html'

class SearchFormView(FormView):
    pass

class UserCreateView(CreateView):
    model = User
    fields = ['user_id', 'password', 'age', 'gender', 'phone', 'email', 'name']
    template_name = 'registration/register.html'
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'

class TemplateView(View):
    template_name = 'home.html'