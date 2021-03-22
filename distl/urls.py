"""distl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import SimpleRouter

from loginsys.views import UserProfileView
from loginsys.views import GroupView
from loginsys.views import SubjectsView
from loginsys.views import TeachersView
from loginsys.views import StudentsView
from loginsys.views import OrganizerView

#        """Импорты для Loginsys"""
from loginsys.views import loginsys_app

#        """Импорты для Blog"""
#        """Импорты для Exam"""
#        """Импорты для HomeWork"""
#        """Импорты для Lectures"""
#        """Импорты для Messenger"""

router = SimpleRouter()

#        """Приложение Loginsys"""
router.register('api/profiles', UserProfileView)
router.register('api/groups', GroupView)
router.register('api/subjects', SubjectsView)
router.register('api/teachers', TeachersView)
router.register('api/students', StudentsView)
router.register('api/organizers', OrganizerView)

#       """Приложение Blog"""
#       """Приложение Exam"""
#       """Приложение HomeWork"""
#       """Приложение Lectures"""
#       """Приложение Messenger"""

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', include('glavnaya.urls')),

    path('loginsys_app/', loginsys_app),



    path('homework/', include('homework.urls')),
    path('blog/', include('blog.urls')),
    path('exams/', include('exams.urls')),
    path('lectures/', include('lectures.urls')),
    path('messenger/', include('messenger.urls')),
    path('adminka/', include('adminka.urls')),
    path('loginsys/', include('loginsys.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += router.urls
