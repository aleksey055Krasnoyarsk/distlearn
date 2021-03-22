from django.db import models
from django.db import IntegrityError
from loginsys.models import *


class Message(models.Model):
    """Model of chat"""


    to_user = models.ForeignKey(User, verbose_name="Кому", related_name="to_user", on_delete=models.CASCADE)

    from_user = models.ForeignKey(User, verbose_name="От кого", related_name="from_user", on_delete=models.CASCADE)

    text = models.TextField("Сообщение", max_length=500)
    date = models.DateField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural ="Сообщения"



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.to_user




"""
class Message(models.Model):



    to_id = models.ForeignKey(User, verbose_name="Кому", related_name="to_user", on_delete=models.CASCADE)

    from_id = models.ForeignKey(User, verbose_name="От кого", related_name="from_user", on_delete=models.CASCADE)

    text = models.TextField("Сообщение", max_length=500)
    date = models.DateField("Дата отправки", auto_now_add=True)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural ="Сообщения"



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.to_user
"""