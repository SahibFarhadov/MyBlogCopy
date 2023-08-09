from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import MyUser


class UserForm(ModelForm):
	class Meta:
		model=User
		fields=["first_name","last_name","email"]
	
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields["first_name"].widget.attrs.update({'class':'form-control'})
		self.fields["last_name"].widget.attrs.update({'class':'form-control'})
		self.fields["email"].widget.attrs.update({'class':'form-control'})

class MyUserForm(ModelForm):
	class Meta:
		model=MyUser
		fields=["bio",'sekil',]

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields["bio"].widget.attrs.update({'class':'form-control'})



