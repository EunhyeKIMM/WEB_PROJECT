from review.models import Review
from django import forms



class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['re_title', 'content']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')