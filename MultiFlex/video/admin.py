from django.contrib import admin
from video.models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_type', 'description', 'tag_list') # 사이트에서 출력할 컬럼 목록

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('genre')

    def tag_list(self, obj):
        return '. '.join(o.name for o in obj.genre.all())