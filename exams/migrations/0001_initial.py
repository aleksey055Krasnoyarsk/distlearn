# Generated by Django 3.1.4 on 2021-01-11 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginsys', '0006_remove_groups_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200, verbose_name='Тема')),
                ('appraisal', models.IntegerField(verbose_name='Оценка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginsys.teachers')),
                ('forgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginsys.groups')),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginsys.subjects')),
            ],
        ),
    ]
