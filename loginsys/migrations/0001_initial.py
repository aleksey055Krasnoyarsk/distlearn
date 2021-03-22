# Generated by Django 3.1.4 on 2020-12-15 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=200, verbose_name='Учебная группа')),
            ],
            options={
                'verbose_name': 'Учебная группа',
                'verbose_name_plural': 'Учебные группы',
            },
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(default='', max_length=200, verbose_name='Задача')),
                ('day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], default='1', max_length=2, verbose_name='День')),
                ('month', models.CharField(choices=[('1', 'Январь'), ('2', 'Февраль'), ('3', 'Март'), ('4', 'Апрель'), ('5', 'Май'), ('6', 'Июнь'), ('7', 'Июль'), ('8', 'Август'), ('9', 'Сентябрь'), ('10', 'Октябрь'), ('11', 'Ноябрь'), ('12', 'Декабрь')], default='1', max_length=2, verbose_name='Месяц')),
                ('year', models.CharField(choices=[('[', 2021), ('2', 2022), ('0', 2023), ('2', 2024), ('1', 2025), (',', 2026), (' ', 2027), ('2', 2028), ('0', 2029), ('2', 2030), ('2', 2031), (',', 2032), (' ', 2033), ('2', 2034), ('0', 2035), ('2', 2036), ('3', 2037), (',', 2038), (' ', 2039), ('2', 2040), ('0', 2041), ('2', 2042), ('4', 2043), (',', 2044), (' ', 2045), ('2', 2046), ('0', 2047), ('2', 2048), ('5', 2049), (',', 2050), (' ', 2051), ('2', 2052), ('0', 2053), ('2', 2054), ('6', 2055), (',', 2056), (' ', 2057), ('2', 2058), ('0', 2059), ('2', 2060), ('7', 2061), (',', 2062), (' ', 2063), ('2', 2064), ('0', 2065), ('2', 2066), ('8', 2067), (',', 2068), (' ', 2069), ('2', 2070), ('0', 2071), ('2', 2072), ('9', 2073), (',', 2074), (' ', 2075), ('2', 2076), ('0', 2077), ('3', 2078), ('0', 2079), (',', 2080), (' ', 2081), ('2', 2082), ('0', 2083), ('3', 2084), ('1', 2085), (',', 2086), (' ', 2087), ('2', 2088), ('0', 2089), ('3', 2090), (']', 2091)], default=2021, max_length=4, verbose_name='Год')),
            ],
            options={
                'verbose_name': 'Органайзер',
                'verbose_name_plural': 'Органайзер',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200, verbose_name='Учебная дисциплина')),
            ],
            options={
                'verbose_name': 'Учебная дисциплина',
                'verbose_name_plural': 'Учебные дисциплины',
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='teacher', max_length=200, verbose_name='Статус')),
                ('login', models.CharField(default='', max_length=200, verbose_name='Логин')),
                ('password', models.CharField(default='', max_length=200, verbose_name='Пароль')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО преподавателя')),
                ('position', models.CharField(max_length=200, verbose_name='Должность преподавателя')),
                ('number', models.CharField(blank=True, max_length=11, verbose_name='Контактный телефон')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('education', models.CharField(max_length=200, verbose_name='Образование')),
                ('degree', models.CharField(blank=True, max_length=11, verbose_name='Ученая степень')),
                ('date_b', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('date_j', models.DateField(blank=True, verbose_name='Дата трудоустройства')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='boss', max_length=200, verbose_name='Статус руководителя')),
                ('status_ed', models.CharField(choices=[('1', 'Школа'), ('2', 'СПО'), ('3', 'ВУЗ'), ('4', 'Доп.Образование')], default='1', max_length=2, verbose_name='Статус учебного заведения')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
                ('adress', models.CharField(blank=True, max_length=11, verbose_name='Адрес учебного заведения')),
                ('number', models.CharField(blank=True, max_length=11, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('license', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d/', verbose_name='Лицензия')),
                ('certificate', models.FileField(blank=True, null=True, upload_to='media/%Y/%m/%d/', verbose_name='Свидетельство о государственной аккредитации')),
                ('boss', models.CharField(blank=True, max_length=11, verbose_name='Руководитель учебного заведения')),
                ('login', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Логин')),
            ],
            options={
                'verbose_name': 'Учебное заведение',
                'verbose_name_plural': 'Учебные заведения',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200, verbose_name='ФИО учащегося')),
                ('date', models.DateField(blank=True, verbose_name='Дата рождения')),
                ('parents', models.CharField(max_length=200, verbose_name='Родители')),
                ('number', models.CharField(blank=True, max_length=11, verbose_name='Телефон родителей')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Группа', to='loginsys.groups')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
    ]