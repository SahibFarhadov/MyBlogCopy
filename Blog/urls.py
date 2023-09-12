from django.urls import path
from . import views
from django.views.generic.edit import CreateView


urlpatterns=[
	path("",views.home),
	path("esas",views.home,name="home"),
	path("meqale/<slug:_slug>",views.blog_details,name="blog-details"),
    path("kateqoriya/<slug:_slug>",views.blogs_by_category,name="blogs_by_category"),
    path("meqale_yaz",views.BlogCreateView.as_view(),name="meqale_yaz"),
    path("meqale/yenile/<slug>/",views.BlogUpdateView.as_view(),name="meqale_yenile"),
    path("meqale/sil/<slug:_slug>",views.delete_blog,name="delete_blog"),
    path("meqale/<slug:_slug>/deyerlendirmesayi",views.deyerlendirmesayi,name="deyerlendirmesayi"),
]