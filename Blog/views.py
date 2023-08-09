from django.shortcuts import render,redirect
from .models import Blog,Category
from django.views.generic.edit import CreateView,UpdateView
from .forms import AddBlogForm
from django.contrib.auth.models import User
from Account import views as account_views
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


# blog update view
class BlogUpdateView(UpdateView):
	model=Blog
	form_class=AddBlogForm
	template_name="Blog/meqale_yenile.html"
	success_url="/hesab/hesab-meqaleleri/"

	def dispatch(self,request,*args,**kwargs):
		if not request.user.is_authenticated:
			return redirect("login")
		return super().dispatch(request,*args,**kwargs)

#blog create view
class BlogCreateView(CreateView):
	model=Blog
	template_name="Blog/meqale_yaz.html"
	form_class=AddBlogForm
	success_url="/hesab/hesab-meqaleleri"
	def form_valid(self,form):
		form.instance.user=self.request.user.myuser
		return super().form_valid(form)

	def dispatch(self,request,*args,**kwargs):
		if not request.user.is_authenticated:
			return redirect("login")
		return super().dispatch(request,*args,*kwargs)

#meqale yaz funksiyasi
def meqale_yaz(request):
	errorMessage=""
	context={
		'form':AddBlogForm,
		'errorMessage':errorMessage
	}
	if request.method=="POST":
		titleofblog=request.POST["titleofblog"]
		image=request.POST["image"]
		description=request.POST["description"]
		category=request.POST["category"]
		errorMessage=titleofblog
		return render(request,'Blog/meqale_yaz.html',context)
	
	return render(request,'Blog/meqale_yaz.html',context)


#blog delete function
def delete_blog(request,_slug):
	if request.user.is_authenticated:
		try:
			blog=Blog.objects.get(slug=_slug)
			if blog.user == request.user.myuser:
				blog.delete()
		except ObjectDoesNotExist:
			return account_views.hesab_meqaleleri(request)
	return account_views.hesab_meqaleleri(request)


#home page function
def home(request):
	gosterme_sayi=10
	if request.GET.get("gosterme_sayi"):
		gosterme_sayi=request.GET.get("gosterme_sayi")
	gosterme_elements=[10,20,30]
	blogs=Blog.objects.filter(is_active=True)
	if len(blogs)<=gosterme_elements[0]:
		gosterme_elements=gosterme_elements[:1]
	elif (len(blogs)>gosterme_elements[0]) and (len(blogs)<=gosterme_elements[1]):
		gosterme_elements=gosterme_elements[:2]
	else:
		gosterme_elements=gosterme_elements[:3]
	paginator=Paginator(blogs,gosterme_sayi)
	categories=Category.objects.all()
	page_number=request.GET.get("page")
	page_obj=paginator.get_page(page_number)
	context = {
		"blogs":page_obj,
		"categories":categories,
		"page_obj":page_obj,
		"gosterme_elements":gosterme_elements,
		"gosterme_sayi":int(gosterme_sayi),
	}
	return render(request,"Blog/index.html",context)

#blog details function
def blog_details(request,_slug):
	blog=Blog.objects.get(slug=_slug)
	userBlog=None
	if blog.user is not None:
		userBlog=blog.user.user
	context={
		"blog":blog,
		"userBlog":userBlog
	}
	return render(request,"Blog/blog-details.html",context)

#kateqoriyaya gore blog cekme funksiyasi
def blogs_by_category(request,_slug):
	gosterme_sayi=10
	if request.GET.get("gosterme_sayi"):
		gosterme_sayi=request.GET.get("gosterme_sayi")
	gosterme_elements=[10,20,30]
	blogs=Blog.objects.filter(category__slug=_slug,is_active=True)
	if len(blogs)<=gosterme_elements[0]:
		gosterme_elements=gosterme_elements[:1]
	elif (len(blogs)>gosterme_elements[0]) and (len(blogs)<=gosterme_elements[1]):
		gosterme_elements=gosterme_elements[:2]
	else:
		gosterme_elements=gosterme_elements[:3]
	paginator=Paginator(blogs,gosterme_sayi)
	page_number=request.GET.get("page")
	page_obj=paginator.get_page(page_number)
	categories = Category.objects.all()
	selectedCategory=Category.objects.get(slug=_slug)
	context={
		"blogs":page_obj,
		"categories":categories,
		"selectedCategory":selectedCategory,
		"page_obj":page_obj,
		"gosterme_elements":gosterme_elements,
		"gosterme_sayi":int(gosterme_sayi),
	}
	return render(request,"Blog/blogs_by_category.html",context)
