from django import forms
from .models import Blog

class AddBlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields=("titleofblog","image","description","is_active","is_home","category")
		widgets={
			'titleofblog':forms.TextInput(attrs={'class':'form-control'}),
		}