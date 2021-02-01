from django.contrib import admin
from .models import Video
# Register your models here.

@admin.register(Video)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_type') # 영화 목록에 보여야 할 목록(추가예정)

