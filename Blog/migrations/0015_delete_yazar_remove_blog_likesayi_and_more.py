# Generated by Django 4.2.2 on 2023-07-02 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_blog_sevimlisayi'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Yazar',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='likeSayi',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='sevimliSayi',
        ),
    ]