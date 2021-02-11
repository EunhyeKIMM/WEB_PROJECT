from review.models import Review
from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model



class MyPage_reView(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['video_id', 're_title', 'user_id']

class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control',}),)
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')

                
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'age', 'gender','phone']
