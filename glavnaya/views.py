from django.shortcuts import render

# Create your views here.

def glavnaya(request):
    return render(request, 'glavnaya/page.html')