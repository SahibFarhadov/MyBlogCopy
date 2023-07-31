from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from Blog.models import Blog
from .forms import UserForm,MyUserForm
import re
from django.core.paginator import Paginator

def meqale_sirala(request,order_by):
	return hesab_meqaleleri(request,order_by)

def hesab(request):
	if request.user.is_authenticated:
		user_form=UserForm(instance=request.user)
		myuser_form=MyUserForm(instance=request.user.myuser)
		context={
			'is_hesab':True,
			'user_form':user_form,
			'myuser_form':myuser_form,
			'message':""
		}
		if request.method=="POST":
			user_form=UserForm(request.POST,instance=request.user)
			myuser_form=MyUserForm(request.POST,instance=request.user.myuser)
			user_form.save()
			myuser_form.save()
			context['message']="Məlumatlar uğurla yeniləndi."
			return render(request,"account/hesab.html",context)

		return render(request,"account/hesab.html",context)
	return redirect("login")

def hesab_meqaleleri(request,order_by="borndatedec"):
	if request.user.is_authenticated:
		order_by1=""
		if order_by=="titleofblogAZ":
			order_by1="titleofblog"
		elif order_by=="titleofblogZA":
			order_by1="-titleofblog"
		elif order_by=="titleofblogZA":
			order_by1="-titleofblog"
		elif order_by=="borndateacs":
			order_by1="borndate"
		elif order_by=="borndatedec":
			order_by1="-borndate"
		elif order_by=="lastmodifiedacs":
			order_by1="lastmodified"
		elif order_by=="lastmodifieddec":
			order_by1="-lastmodified"
		gosterme_sayi=10
		if request.GET.get("gosterme_sayi"):
			gosterme_sayi=request.GET.get("gosterme_sayi")
		gosterme_elements=[10,20,30]
		blogs=Blog.objects.filter(user=request.user.myuser) # request eden user ile blogun useri eyni oldugunu yoxlayir
		myblogs=blogs.order_by(order_by1)
		if len(blogs)<=gosterme_elements[0]:
			gosterme_elements=gosterme_elements[:1]
		paginator = Paginator(myblogs,gosterme_sayi)
		page_number=request.GET.get("page")
		page_obj=paginator.get_page(page_number)
		context={
			"blogs":page_obj,
			"is_meqalelerim":True,
			"sort_string":order_by,
			"page_obj":page_obj,
			"gosterme_elements":gosterme_elements,
			"gosterme_sayi":int(gosterme_sayi),
		}
		return render(request,"account/blog_in_hesab.html",context)
	return redirect("login")

#account app ucun login metodu
def login_request(request):
	if request.user.is_authenticated:
		return redirect("home")
	if request.method=="POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect("home")
		else:
			return render(request,"account/login.html",{
				"error":"İstifadəçi adı və ya parol yanlışdır",
				"username":username
				})
	return render(request,"account/login.html")

# account app ucun register metodu
def register_request(request):

	if request.user.is_authenticated:
		return redirect("home")
	if request.method=="POST":
		name=request.POST["name"]
		surname=request.POST["surname"]
		nickname=request.POST["nickname"]
		email=request.POST["email"]
		password=request.POST["password"]
		repassword=request.POST["repassword"]
		name=name.capitalize()
		surname=surname.capitalize()

		errorMessage=""
		dataKeep={
			"name":name,
			"surname":surname,
			"nickname":nickname,
			"email":email,
			"errorMessage":errorMessage
		}

		if (password==repassword):
			if len(password)<8: #parolun uzunlugunun yoxlanilmasi
				dataKeep["errorMessage"]="Şifrə 8-dən qısadır"
				return render(request,"account/register.html", dataKeep)
			elif re.search(name.lower(),password.lower()) is not None:  # Parolda istifadəçi adının istifadə edilməsi
				dataKeep["errorMessage"]="Şifrədə adınızdan istifadə edə bilməzsiniz"
				return render(request,"account/register.html", dataKeep)
			elif len(password)>=8:
				if User.objects.filter(username=nickname).exists():
					dataKeep["errorMessage"]="Daxil edilən istifadəçi adı artıq mövcuddur"
					return render(request, "account/register.html", dataKeep )
				elif User.objects.filter(email=email).exists():
					dataKeep["errorMessage"]="Daxil edilən email ünvanı artıq istifadə edilmişdir"
					return render(request, "account/register.html", dataKeep )
				else:
					user=User.objects.create_user(username=nickname,first_name=name,last_name=surname,password=password,email=email)
					return redirect("login")	
	return render(request,"account/register.html")

#account app ucun logout metodu
def logout_request(request):
	logout(request)
	return redirect("home")



#parolu yoxlamaq ucun proqramdir tuple qaytarir. Birinci deyeri True or False ikinci deyeri string formatindan error mesaji qaytarir
def paroluYoxla(parol,ad):
	yoxlama=re.search(ad, parol)
	if len(parol)<8: #parolun uzunlugunun yoxlanilmasi
		return (False,"Parol 8-dən qısadır")
	elif yoxlama is None: # Parolda istifadəçi adının istifadə edilməsi
		return (False, "Parolda adınızdan istifadə edə bilməzsiniz")
	else:
		return (True,"ok")
