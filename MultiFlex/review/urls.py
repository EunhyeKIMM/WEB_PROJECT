from django.urls import path, re_path 
from review.views import *

app_name = 'review'

urlpatterns = [

     path('<int:pk>/updateReview/', ReviewUpdateView.as_view(), name="update_review"), 

     path('<int:pk>/deleteReview/', ReviewDeleteView.as_view(), name="delete_review"),

     path('<int:pk>/updateComment/', CommentUpdateView.as_view(), name="update_comment"),

     path('<int:pk>/deleteComment/', CommentDeleteView.as_view(), name="delete_comment"),

     
     #review_detail
     path('<int:pk>/', ReviewDV.as_view(), name='review_detail'),
     
     #review/add
     #path('add/', CommentCV.as_view(), name='add'), 
]