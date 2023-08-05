from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from Account.models import MyUser

class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name="Kateqoriya adı")
    slug=models.SlugField(null=False, editable=False,unique=True,db_index=True)
    
    def __str__(self):
        return f"{self.name}"

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

class Blog(models.Model):
    titleofblog = models.CharField(max_length=150,verbose_name="Başlıq",blank=False)
    image = models.ImageField(upload_to="blogs/%Y/%m",verbose_name="Şəkil")
    description = RichTextUploadingField(config_name="fullconfig")
    is_active = models.BooleanField(verbose_name="Aktiv status")
    is_home = models.BooleanField(verbose_name="Ana səhifə aktiv")
    slug = models.SlugField(editable=False,unique=True,db_index=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,verbose_name="Kateqoriya seç")
    lastmodified = models.DateTimeField("Sonuncu deyişiklik tarixi",auto_now=True,blank=True,null=True)
    borndate = models.DateTimeField("Yaranma tarixi",auto_now_add=True,blank=True,null=True)
    snippet = models.CharField(max_length=50,default="Davamını oxumaq üçün klikləyin...",blank=True,null=True)
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.titleofblog
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.titleofblog)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("home")