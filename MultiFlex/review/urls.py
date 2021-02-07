from django.urls import path, re_path 
from review.views import *

app_name = 'review'

urlpatterns = [
     path('addReview/', ReviewCreateView.as_view(), name="add_review"), 

     path('<int:pk>/updateReview/', ReviewUpdateView.as_view(), name="update_review"), 

     path('<int:pk>/deleteReview/', ReviewDeleteView.as_view(), name="delete_review"), 
]