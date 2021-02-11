from django.views.generic import UpdateView, DeleteView
from review.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 
from video.models import *
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.views.generic.edit import FormMixin

class ReviewUpdateView(UpdateView, OwnerOnlyMixin):
    model = Review
    template_name = 'review/review_upload_form.html'
    fields = ['re_title', 'content' ]

    def get_success_url(self):
        return reverse('video:video_detail', kwargs={'pk':self.object.video_id_id})


class ReviewDeleteView(DeleteView, OwnerOnlyMixin):
    model = Review
    template_name = 'review/review_delete_confirm.html'
    success_url = reverse_lazy('review:add_review')

    def get_success_url(self):
        return reverse('video:video_detail', kwargs={'pk':self.object.video_id_id})

class ReviewDV(DetailView,FormMixin):
    model = Review
    template_name = 'review/review_detail.html'
    context_object_name = 'review'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # count_view = self.get_object()
        # if count_view.owner != self.request.user:
        #     count_view.read_cnt = count_view.read_cnt + 1
        #     count_view.save()
        review = context['review']
        comment_list = review.comment_set.all()
        context['comment_list']= comment_list
        context['form'] = CommentForm(initial={'text':'',})
        context['user_id'] = self.request.user        
        return context
  
    def get_success_url(self):
        return reverse('review:review_detail', kwargs={'pk':self.object.pk})
    
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        dat = form.save(commit=False)
        dat.document = get_object_or_404(Review, pk=self.object.pk)
        dat.author = self.request.user
        dat.save()
        return super(ReviewDV, self).form_valid(form)


class ReviewList(ListView):
    model = Review
    template_name = 'review/myreview.html'
    paginate_by = 10

    def get_queryset(self):
        # return Review.objects.all()
        return Review.objects.filter(user_id = self.request.user)


# class CommentCV(LoginRequiredMixin,CreateView): #redirect로 action동작에 연결해준다
#     http_method_names = ['post']
#     model = Comment
#     fields = ['document','author','text']# 포린키에 맞춰서 추가
#     #success_url = reverse_lazy('review:review_detail')

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         # return HttpResponseRedirect(self.get_success_url)
#         return super().form_valid(form)
         

#     def get_success_url(self):
#         return  reverse_lazy('review:review_detail',kwargs={'pk':self.comment.pk})# pk에 맞춰서 id 줘야함