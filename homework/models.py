from django.db import models
from django.utils import timezone
from loginsys.models import Groups, Subjects, Teachers

# Create your models here.


class Task(models.Model):
    forgroup = models.ForeignKey(Groups, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    author = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    class Meta:
        verbose_name ='Домашнее задание'
        verbose_name_plural = 'Домашние задания'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


