from django.db.models import fields
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, TemplateView,
                                FormView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from video.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 


class VideoUploadView(CreateView):
    model = Video
    template_name = 'video/video_upload_form.html'
    fields = ['title', 'description', 'genre', 'release_dt', 'running_time', 'director', 'video_type', 'grade', 'video_link' ]
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
        return Video.objects.filter(video_type=self.kwargs.get('video_type'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs.get('video_type')      
        return context

class PhotoView(DetailView):
    model = Video
    fields = ['vthumbnail']

    def get_queryset(self):        
        return Video.objects.filter(video_id=self.kwargs.get('video_id'))


class VideoLV(ListView):
    model = Video
    template_name = 'video/index.html'
    #context_object_name = 'videos' # video_list

# def video_list(request):
#     latest_video_list = Video.objects.all

#     context = {'latest_video_list' : latest_video_list}

#     return render(request, 'video/index.html',context)

class VideoDV(DetailView):
    model = Video
    context_object_name = 'video'
    template_name = 'video/video_detail.html'
    
        
