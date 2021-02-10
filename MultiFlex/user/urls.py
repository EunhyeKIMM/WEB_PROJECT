from django.urls import path
from user import views
from mysite.views import UserCreateDoneTV


urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/done/', UserCreateDoneTV.as_view(), name='register_done'),
    # path('login/', views.login, name='login'),            # 나중에 혼자하는거.
    # path('logout/', views.logout, name='logout'),  
]