from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from loginsys.models import Groups, Subjects, Teachers

# Create your models here.


class Exam(models.Model):
    forgroup = models.ForeignKey(Groups, on_delete=models.CASCADE)
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    author = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    theme = models.CharField(verbose_name='Тема', max_length=200)
    appraisal = models.IntegerField(verbose_name='Оценка', default=1, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])



    class Meta:
        verbose_name ='Тест'
        verbose_name_plural = 'Тесты'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.theme