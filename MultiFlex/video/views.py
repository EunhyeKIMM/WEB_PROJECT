from django.shortcuts import render
from django.views.generic import (ListView, DetailView, TemplateView,
                                FormView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from video.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 





class VideoUploadView(LoginRequiredMixin, CreateView):
    model = Video
  

class VideoUpdateView(OwnerOnlyMixin, UpdateView):
    model = Video
  


class VideoDeleteView(OwnerOnlyMixin, DeleteView):
    model = Video
 

