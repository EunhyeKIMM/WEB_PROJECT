from django.shortcuts import render
from django.views.generic import (ListView, DetailView, TemplateView,
                                FormView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from review.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 
from video.models import *


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

class ReviewDV(DetailView):
    model = Review
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        count_view = self.get_object()
        if count_view.owner != self.request.user:
            count_view.read_cnt = count_view.read_cnt + 1
            count_view.save()
        return context