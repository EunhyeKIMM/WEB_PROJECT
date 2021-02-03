from django.urls import path, re_path 
from video.views import *

app_name = 'video'

urlpatterns = [
     path('uploadVideo/', VideoUploadView.as_view(), name="upload_Video"), 

     path('<int:pk>/updateVideo/', VideoUpdateView.as_view(), name="update_Video"), 

     path('<int:pk>/deleteVideo/', VideoDeleteView.as_view(), name="delete_Video"), 
]