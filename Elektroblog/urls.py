from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('panel/', admin.site.urls),
    path('',include('Blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('hesab/',include('Account.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
