from django.urls import path
from mysite.views import UserCreateDoneTV
from user import views
from review.views import ReviewList
from mysite.views import UserCreateDoneTV


urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    path('myreview/', ReviewList.as_view(), name='myreview'),
    path('', views.userPage, name='mypage'),
    path('change_password/', views.change_password, name='change_password'),
    path('delete/', views.delete, name='user_delete'),
    path('update/', views.update, name='user_update'),
]



    # path('login/', views.login, name='login'),            # 나중에 혼자하는거.
    # path('logout/', views.logout, name='logout'),
