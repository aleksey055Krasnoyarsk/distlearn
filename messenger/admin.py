from django.contrib import admin

# Register your models here.
from .models import Message



class MessageAdmin(admin.ModelAdmin):
    """Диалоги"""

    list_display = ("from_user", "to_user", "text", "date")


admin.site.register(Message, MessageAdmin)

