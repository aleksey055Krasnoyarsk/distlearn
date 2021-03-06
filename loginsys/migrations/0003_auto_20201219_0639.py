# Generated by Django 3.1.4 on 2020-12-19 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20201218_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1', 'Преподаватель'), ('2', 'Студент'), ('3', 'Руководитель')], default='3', max_length=2, verbose_name='Статус')),
                ('login', models.CharField(default='boss', max_length=200, verbose_name='Логин руководителя')),
                ('url_for_mess', models.SlugField(default='', max_length=200)),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='login',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]
