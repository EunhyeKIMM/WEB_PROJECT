from django.urls import path
from user import views

# app_name = 'user' 

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),            # 나중에 혼자하는거.
    # path('logout/', views.logout, name='logout'),
    path('', views.userpage, name='mypage'),
    # path('mypage_info/', views.userinfo, name='mypage_info'),
]