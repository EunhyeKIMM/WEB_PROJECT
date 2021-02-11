from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, TemplateView,
                                FormView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from video.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 
from django.core.paginator import Paginator
from review.models import *
from video.form import ReviewForm
from user.models import * 
from .form import *
from django.db.models import Q
import json 
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

class VideoUploadView(CreateView, LoginRequiredMixin):
    model = Video
    template_name = 'video/video_upload_form.html'
    fields = ['title', 'description', 'genre', 'release_dt', 'running_time', 'director', 'video_type', 'grade', 'video_link', 'video_thumb' ]
    success_url = reverse_lazy('video:upload_Video') # 추후에 Detail로 변경 


class VideoUpdateView(UpdateView):
    model = Video
    template_name = 'video/video_upload_form.html'
    fields = ['title', 'description', 'genre', 'release_dt', 'running_time', 'director', 'video_type', 'grade' ]
    
    def get_success_url(self):
        return reverse('video:video_detail', kwargs={'pk':self.object.video_id})


class VideoDeleteView(DeleteView):
    model = Video
    template_name = 'video/video_delete_confirm.html'
    success_url = reverse_lazy('video:upload_Video') # Index 페이지로 바꿔야 함. 


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

class VideoDV(DetailView, FormMixin, LoginRequiredMixin):
    model = Video
    context_object_name = 'video'
    template_name = 'video/video_detail.html'
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('video:video_detail', kwargs={'pk':self.object.pk})
   
    # Detail View에서는 paginate_by없기 때문에 만들어줘야 한다
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = context['video']
        review_list = video.review_set.all().order_by('-create_dt')   #.order_by('-create_dt')[:5]
        paginator = Paginator(review_list, 2) #한 페이지에 보여줄 개수 
        
        page_number = self.request.GET.get('page') # 현재 페이지 받아옴
        page_obj = paginator.get_page(page_number) # 현재 페이지에 있는 목록 

        context['paginator'] = paginator
        context['page_obj'] = page_obj #페이지 목록

        context['form'] = ReviewForm(initial={'re_title':'','text': '',})   
        context['user_id'] = self.request.user 
        context['reviews'] = self.object.review_set.all() 
        dvdv = self.get_object()
        if dvdv.bookmark.filter(id=self.request.user.id).exists():
            context['how_dib'] = "찜하기 취소"
        else:
            context['how_dib'] = "찜하기"

        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.video_id = get_object_or_404(Video, pk=self.object.pk)
        comment.user_id = self.request.user
        comment.save() 
        return super(VideoDV, self).form_valid(form)

# 좋아요 기능 함수 
@login_required
@require_POST
def like(request):
    pk = request.POST.get('pk', None)
    video = get_object_or_404(Video, pk=pk)
    user = request.user

    if video.recommend.filter(id=user.id).exists():
        video.recommend.remove(user)
        video.like -= 1
        video.save()
    else: 
        video.recommend.add(user)
        video.like += 1
        video.save()
    context = {'like_count': video.count_like_user()}
 
    return HttpResponse(json.dumps(context), content_type="application/json")

# 찜하기 기능 함수 
@login_required
@require_POST
def dibs(request):
    pk = request.POST.get('pk', None)
    video = get_object_or_404(Video, pk=pk)
    user = request.user

    if video.bookmark.filter(id=user.id).exists():
        video.bookmark.remove(user)
        message = " "
    else: 
        video.bookmark.add(user)
        message = " 취소"
    context = {'message': message}
 
    return HttpResponse(json.dumps(context), content_type="application/json")



class SearchView(FormView):
    model = Video 
    template_name = 'video/search.html'
    form_class = PostSearchForm

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        video_list = Video.objects.filter(
            Q(title__icontains=searchWord) |
            Q(director__icontains=searchWord)
        ).distinct()
        
        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = video_list

        return render(self.request, self.template_name, context)
    

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

       
class DibsView(ListView, LoginRequiredMixin):
    model = Video
    template_name = 'video/video_dibs.html'

    def get_queryset(self):
        return Video.objects.filter(bookmark=self.request.user)
