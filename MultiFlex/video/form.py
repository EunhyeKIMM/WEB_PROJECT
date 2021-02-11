from review.models import Review
from django import forms
from review.models import Comment



class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['re_title', 'content']



class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='검색어를 입력하세요.')

