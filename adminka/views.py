from django.shortcuts import render

# Create your views here.

def adminka(request):
    return render(request, 'adminka/page.html')

def cabinet_of_UserProfile(request):
    return render(request, 'adminka/page_UserProfile.html')

def cabinet_of_Group(request):
    return render(request, 'adminka/page_cabinet_of_Group.html')

def cabinet_of_Teacher(request):
    return render(request, 'adminka/page_Teacher.html')

def cabinet_of_Student(request):
    return render(request, 'adminka/page_Student.html')