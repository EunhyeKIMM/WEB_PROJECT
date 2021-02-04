from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('uploadVideo/', VideoUploadView.as_view(), name="upload_Video"), 

    path('<int:pk>/updateVideo/', VideoUpdateView.as_view(), name="update_Video"), 

    path('<int:pk>/deleteVideo/', VideoDeleteView.as_view(), name="delete_Video"),

    path('<str:video_type>/videoList/', VideoTypeView.as_view(), name="show_video_type"), 
    # 실험
    path('',views.VideoLV.as_view(), name='index'),
    # detail
    path('<int:pk>/', views.VideoDV.as_view(), name='video_detail'),
]