from review.models import Review
from django import forms



class MyPage_reView(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['video_id', 're_title', 'user_id']