from django.contrib import admin
from .models import Review


@admin.register(Review)
# 리뷰 리스트에서 보이는 목록들.
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('re_id', 're_title', 'like')    

