from django.contrib import admin
from video.models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_type', 'description') # 사이트에서 출력할 컬럼 목록