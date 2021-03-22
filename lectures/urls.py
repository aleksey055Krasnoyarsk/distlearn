from django.urls import path
from . import views

urlpatterns = [
    path('lectures/', views.lectures, name="lectures"),
]