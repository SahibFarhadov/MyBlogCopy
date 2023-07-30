from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Blog,Category

class BlogAdmin(admin.ModelAdmin):
    list_display=("titleofblog","is_active","is_home","slug")
    list_editable=("is_home","is_active")
    readonly_fields=("slug",)
    list_filter=('category',)

class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","slug")


admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)

admin.site.site_title="Blog saytın paneli"
admin.site.site_header="Blog sayt administrasiyası"