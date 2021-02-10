from django.views.generic import UpdateView, DeleteView
from review.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 
from video.models import *
from django.views.generic import ListView

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

class ReviewList(ListView):
    model = Review
    template_name = 'review/myreview.html'

    def get_queryset(self):
        # return Review.objects.all()
        return Review.objects.filter(user_id = self.request.user)