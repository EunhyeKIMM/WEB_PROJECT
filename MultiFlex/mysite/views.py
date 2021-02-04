from django.views.generic import TemplateView, FormView

class Homeview(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        theme = self.request.GET.get('theme')
        if theme : 
            self.request.session['theme']=theme
        return super().get_context_data(**kwargs)

class SearchFormView(FormView):
    pass