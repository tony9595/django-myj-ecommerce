from django.contrib import admin
from accounts.models import User

# Register your models here.

# 어드민 페이지 등록방법 3가지
# 1. 기본적인 관리자 페이지에서 기본적인 등록
# 커스텀 기능을 (검색 ,필터 ,필드)을 추가할 수 없음
# admin.site.register(User)


# 2. @admin.register 데코레이터 활용


@admin.register(User)
class UserAccountsAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "job", "gender"]
    search_fields = ["username", "email", "job", "gender"]
    list_filter = ["username", "email", "job", "gender"]


# 3. ModelAdmin 클래스를 활요하는 방법(커스텀 가능)
# admin.site.register(User, UserAccountsAdmin)