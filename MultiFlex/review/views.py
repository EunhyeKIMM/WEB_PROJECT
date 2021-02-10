from django.views.generic import UpdateView, DeleteView
from review.models import *
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin 
from video.models import *


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
