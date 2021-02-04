from django.shortcuts import  get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from video.models import Video

# Create your views here.

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
    
        