from django.shortcuts import render
from django.views.generic import (ListView, DetailView, TemplateView,
                                FormView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from review.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 
from video.models import *


# 비디오디테일 성공 시 삭제 
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review/review_upload_form.html'
    fields = ['re_title', 'content' ]
    success_url = reverse_lazy('video.get_absolute_url') 

    def form_invalid(self, form):
        # return HttpResponseRedirect(self.get_success_url())
        response = super().form_valid(form) # Review 모델 저장, self.object

    def get_context_data(self, **kwargs):
        save_fk = self.get_object()
        save_fk.user_id = self.request.user
        return super().get_context_data(**kwargs)


# OwneronlyMixin 추가 해야함 !

class ReviewUpdateView(UpdateView):
    model = Review
    template_name = 'review/review_upload_form.html'
    fields = ['re_title', 'content' ]

    def get_success_url(self):
        return reverse('video:video_detail', kwargs={'pk':self.object.video_id_id})


class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_delete_confirm.html'
    success_url = reverse_lazy('review:add_review')

    def get_success_url(self):
        return reverse('video:video_detail', kwargs={'pk':self.object.video_id_id})
