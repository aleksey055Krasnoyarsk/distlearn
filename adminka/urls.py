from django.urls import path
from . import views

urlpatterns = [
    path('adminka/', views.adminka, name="adminka"),
    path('cabinet_of_UserProfile/', views.cabinet_of_UserProfile, name="cabinet_of_UserProfile"),
    path('cabinet_of_Group/', views.cabinet_of_Group, name="cabinet_of_Group"),
    path('cabinet_of_Teacher/', views.cabinet_of_Teacher, name="cabinet_of_Teacher"),
    path('cabinet_of_Student/', views.cabinet_of_Student, name="cabinet_of_Student"),
]