from django.contrib import admin
from user.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'bookmark') # 사이트에서 출력할 컬럼 목록