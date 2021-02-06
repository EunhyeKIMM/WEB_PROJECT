from django.shortcuts import render
from django.views.generic import (ListView, DetailView, TemplateView,
                                FormView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from review.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 





class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review/review_upload_form.html'
    fields = ['re_title', 'content' ]
    success_url = reverse_lazy('review:update_review') # 추후에 Detail로 변경 

    def form_invalid(self, form):
        # form.instance.user_id_id = 2
        # form.instance.video_id_id = 8
        # return HttpResponseRedirect(self.get_success_url())
        response = super().form_valid(form) # Review 모델 저장, self.object


class ReviewUpdateView(OwnerOnlyMixin, UpdateView):
    model = Review
    template_name = 'review/review_upload_form.html'
    fields = ['re_title', 'content' ]
    success_url = reverse_lazy('review:add_review')


class ReviewDeleteView(OwnerOnlyMixin, DeleteView):
    model = Review
    template_name = 'review/review_delete_confirm.html'
    success_url = reverse_lazy('review:add_review')

