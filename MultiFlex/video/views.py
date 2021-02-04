from django.shortcuts import render
from django.views.generic import (ListView, DetailView, TemplateView,
                                FormView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from video.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 





class VideoUploadView(CreateView):
    model = Video
    template_name = 'video/video_upload_form.html'
    fields = ['title', 'description', 'genre', 'release_dt', 'running_time', 'director', 'video_type', 'grade' ]
    success_url = reverse_lazy('video:upload_Video') # 추후에 Detail로 변경 


class VideoUpdateView(UpdateView):
    model = Video
    template_name = 'video/video_upload_form.html'
    fields = ['title', 'description', 'genre', 'release_dt', 'running_time', 'director', 'video_type', 'grade' ]
    success_url = reverse_lazy('video:upload_Video')


class VideoDeleteView(DeleteView):
    model = Video
    template_name = 'video/video_delete_confirm.html'
    success_url = reverse_lazy('video:upload_Video')


# 상단 메뉴바에서 영화나 드라마로 분류된 페이지
class VideoTypeView(ListView):
    model = Video
    template_name = 'video/video_type.html'

    def get_queryset(self):
        # some = self.kwargs
        return Video.objects.filter(video_type=self.kwargs.get('video_type'))