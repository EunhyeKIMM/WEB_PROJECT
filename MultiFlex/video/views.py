from django.db.models import fields
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, TemplateView,
                                FormView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from video.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 
from django.core.paginator import Paginator


class VideoUploadView(CreateView):
    model = Video
    template_name = 'video/video_upload_form.html'
    fields = ['title', 'description', 'genre', 'release_dt', 'running_time', 'director', 'video_type', 'grade', 'video_link', 'video_thumb' ]
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
    success_url = reverse_lazy('video:video_detail')

    def get_queryset(self):
        return Video.objects.filter(video_type=self.kwargs.get('video_type'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = self.kwargs.get('video_type')      
        return context


class VideoLV(ListView):
    model = Video
    template_name = 'video/index.html'
    #context_object_name = 'videos' # video_list
    context_object_name='videos'
    
# def video_list(request):
#     latest_video_list = Video.objects.all

#     context = {'latest_video_list' : latest_video_list}

#     return render(request, 'video/index.html',context)

class VideoDV(DetailView):
    model = Video
    context_object_name = 'video'
    template_name = 'video/video_detail.html'
   
    # Detail View에서는 paginate_by없기 때문에 만들어줘야 한다
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = context['video']
        review_list = video.review_set.all()   #.order_by('-create_dt')[:5]
        paginator = Paginator(review_list, 2) #한 페이지에 보여줄 개수 
        
        page_number = self.request.GET.get('page') # 현재 페이지 받아옴
        page_obj = paginator.get_page(page_number) # 현재 페이지에 있는 목록 

        context['paginator'] = paginator
        context['page_obj'] = page_obj #페이지 목록
        return context



class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_video_list.html'
    model = Video

    def get_queryset(self):
        return Video.objects.filter(genre__name=self.kwargs.get('tag'))
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context

       
        
    
        
