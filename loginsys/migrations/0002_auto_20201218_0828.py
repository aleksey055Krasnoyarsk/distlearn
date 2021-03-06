# Generated by Django 3.1.4 on 2020-12-18 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='login',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Логин'),
        ),
        migrations.AddField(
            model_name='students',
            name='url_for_mess',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='teachers',
            name='url_for_mess',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='url_for_mess',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='login',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='login',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Логин'),
        ),
    ]
