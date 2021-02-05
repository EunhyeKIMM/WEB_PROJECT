from django.shortcuts import  get_object_or_404, render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from video.models import Video
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.

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


       
        
    
        