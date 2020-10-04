from django.shortcuts import render

def base(request):
    return render(request, 'base/base.html')

def about(request):
    return render(request, 'base/about.html') 
       