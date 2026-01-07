from django.contrib import admin
from .models import Post, Comment

# 관리자 페이지에서 게시글의 제목, 카테고리, 작성일을 바로 볼 수 있게 설정
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    list_filter = ('category',) # 오른쪽 사이드바에서 카테고리별 필터 기능 추가

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)