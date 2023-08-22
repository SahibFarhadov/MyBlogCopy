from django.db import models
from uuid import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class MyUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True)
    sekil=models.ImageField("Şəkil",upload_to="main/uploads/myuser/images/%d/%m/%Y",null=True,blank=True,default="rootstatic/img/default-man.jpg")

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_myuser(sender, instance, created, **kwargs):
    if created:
        MyUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_myuser(sender, instance, **kwargs):
    instance.myuser.save()
