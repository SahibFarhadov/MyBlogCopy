from django.urls import path
from . import views

urlpatterns=[
	path('daxil_ol',views.login_request,name='login'),
	path('qeydiyyatdan_kec',views.register_request,name='register'),
	path('hesabdan_cix',views.logout_request,name='logout'),
	path("menim-hesabim/",views.hesab,name="profile"),
	path("hesab-meqaleleri/",views.hesab_meqaleleri,name="hesab_meqaleleri"),
	path('meqale-sirala/<str:order_by>',views.meqale_sirala,name="meqale_sirala")
]