from django.urls import path
from . import views

urlpatterns = [
    path('loginsys/', views.loginsys, name="loginsys"),
]
