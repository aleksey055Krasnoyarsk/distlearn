from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone
from loginsys.choices import *
# Create your models here.

class UserProfile(models.Model):
    status = models.CharField(verbose_name='Статус руководителя', max_length=200, default='boss')
    SCHOOL = '1'
    COLLEGE = '2'
    UNIVERSITY = '3'
    POSTDIPLOMA = '4'
    login = models.ForeignKey(User, verbose_name="Логин", on_delete=models.CASCADE, default='')
    STATUS_CHOICES = (
        (SCHOOL, 'Школа'),
        (COLLEGE, 'СПО'),
        (UNIVERSITY, 'ВУЗ'),
        (POSTDIPLOMA, 'Доп.Образование'),
    )
    status_ed = models.CharField(verbose_name='Статус учебного заведения',
        max_length=2,
        choices = STATUS_CHOICES,
        default=SCHOOL,)
    name = models.CharField(verbose_name="Наименование", max_length=200)
    adress = models.CharField(verbose_name='Адрес учебного заведения', max_length=11, blank=True)
    number = models.CharField(verbose_name='Номер телефона', max_length=11, blank=True)
    email = models.EmailField(verbose_name='email address', blank=True)
    license = models.FileField(upload_to='media/%Y/%m/%d/', null=True, blank=True, verbose_name="Лицензия")
    certificate = models.FileField(upload_to='media/%Y/%m/%d/', null=True, blank=True, verbose_name="Свидетельство о государственной аккредитации")
    boss = models.CharField(verbose_name='Руководитель учебного заведения', max_length=11, blank=True)
    url_for_mess = models.SlugField(max_length=200,  default='')


    class Meta:
        verbose_name ='Учебное заведение'
        verbose_name_plural = 'Учебные заведения'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name



class Groups(models.Model):
    group = models.CharField(verbose_name='Учебная группа', max_length=200)

    class Meta:
        verbose_name ='Учебная группа'
        verbose_name_plural = 'Учебные группы'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.group


class Subjects(models.Model):
    subject = models.CharField(verbose_name='Учебная дисциплина', max_length=200)



    class Meta:
        verbose_name ='Учебная дисциплина'
        verbose_name_plural = 'Учебные дисциплины'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subject


class Teachers(models.Model):
    status = models.CharField(verbose_name='Статус', max_length=200, default='teacher')
    login = models.CharField(verbose_name="Логин", max_length=200, default='')
    password = models.CharField(verbose_name='Пароль', max_length=200, default='')
    fio = models.CharField(verbose_name='ФИО преподавателя', max_length=200)
    position = models.CharField(verbose_name='Должность преподавателя', max_length=200)
    number = models.CharField(verbose_name='Контактный телефон', max_length=11, blank=True)
    email = models.EmailField(verbose_name='email address', blank=True)
    education = models.CharField(verbose_name='Образование', max_length=200)
    degree = models.CharField(verbose_name='Ученая степень', max_length=11, blank=True)
    date_b = models.DateField(verbose_name='Дата рождения', blank=True)
    date_j = models.DateField(verbose_name='Дата трудоустройства', blank=True)
    url_for_mess = models.SlugField(max_length=200, default='')




    class Meta:
        verbose_name ='Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.fio

class Students(models.Model):
    login = models.CharField(verbose_name="Логин", max_length=200, default='')
    fio = models.CharField(verbose_name='ФИО учащегося', max_length=200)
    date = models.DateField(verbose_name='Дата рождения', blank=True)
    parents = models.CharField(verbose_name='Родители', max_length=200)
    number = models.CharField(verbose_name='Телефон родителей', max_length=11, blank=True)
    group = models.ForeignKey(Groups, related_name='Группа', on_delete=models.CASCADE)
    url_for_mess = models.SlugField(max_length=200,default='')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.fio


class Organizer(models.Model):
    task = models.CharField(verbose_name='Задача', max_length=200, default='')

    day = models.CharField(
        max_length=2,
        verbose_name='День',
        choices=DAY_CHOICES,
        default='1',
    )
    month = models.CharField(
       max_length=2,
       verbose_name='Месяц',
       choices=MONTH_CHOICES,
       default=JANUARY,
    )
    year = models.CharField(
        max_length=4,
        verbose_name='Год',
        choices=YEAR_CHOICES,
        default=a[0],
    )


    class Meta:
        verbose_name ='Органайзер'
        verbose_name_plural = 'Органайзер'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.task