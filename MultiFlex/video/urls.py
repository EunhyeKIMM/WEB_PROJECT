from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    # 실험
    path('',views.VideoLV.as_view(), name='index'),
    # detail
    path('<int:pk>/', views.VideoDV.as_view(), name='video_detail'),
    
]