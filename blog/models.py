from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name="Логин", on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    class Meta:
        verbose_name ='Блог'
        verbose_name_plural = 'Блоги'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title





