from django import forms
from .models import Blog

class AddBlogForm(forms.ModelForm):
	class Meta:
		model = Blog
		fields=("titleofblog","image","description","is_active","is_home","category")
		widgets={
			'titleofblog':forms.TextInput(attrs={'class':'form-control','oninvalid':'check_titleofblog()','onvalid':'check_titleofblog_valid()'}),
			'image': forms.FileInput(attrs={'class':'form-control','oninvalid':'check_image()'}),
			'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
			'is_home': forms.CheckboxInput(attrs={'class':'form-check-input'}),
			'category': forms.Select(attrs={'class':'form-select'}),
		}