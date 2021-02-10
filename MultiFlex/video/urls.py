from django.urls import path
from video.views import *


app_name = 'video'

urlpatterns = [
    path('uploadVideo/', VideoUploadView.as_view(), name="upload_Video"), 

    path('<int:pk>/', VideoDV.as_view(), name='video_detail'),

    path('<int:pk>/updateVideo/', VideoUpdateView.as_view(), name="update_Video"), 

    path('<int:pk>/deleteVideo/', VideoDeleteView.as_view(), name="delete_Video"),

    path('<str:video_type>/videoList/', VideoTypeView.as_view(), name="show_video_type"), 
    # 실험
    path('', VideoLV.as_view(), name='index'),
    # detail
    path('<int:pk>/', VideoDV.as_view(), name='video_detail'),

    path('searchVideo/', SearchView.as_view(), name='search_video'),

    path('like/', like, name='video_like'),
    
    path('dibs/', dibs, name='video_dibs'),

    path('tag/', TagCloudTV.as_view(), name='tag_cloud'),

    path('tag/<str:tag>/', TaggedObjectLV.as_view(), name='tagged_object_list'),
    
    path('mydibs/', DibsView.as_view(), name='dibs_list'),
]