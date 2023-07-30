# Generated by Django 4.2.2 on 2023-07-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0018_rename_title_blog_titleofblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='lastmodified',
            field=models.DateField(auto_now=True, null=True, verbose_name='Sonuncu deyişiklik tarixi'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='snippet',
            field=models.CharField(blank=True, default='Davamını oxumaq üçün klikləyin...', max_length=50, null=True),
        ),
    ]
