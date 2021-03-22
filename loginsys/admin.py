from django.contrib import admin

from .models import UserProfile
from .models import Groups
from .models import Subjects
from .models import Teachers
from .models import Students

from .models import Organizer
# Register your models here.



admin.site.register(UserProfile)
admin.site.register(Groups)
admin.site.register(Subjects)
admin.site.register(Teachers)
admin.site.register(Students)

admin.site.register(Organizer)