from django.shortcuts import render

def index(request):
    return render(request,'personal/blog/blog.html')

def about(request):
    return render(request,'personal/about.html')

def login(request):
    return render(request,'personal/form.html')

def menu(request):
    return render(request,'personal/menu.html')

def catering(request):
    return render(request,'personal/catering.html')

def contact(request):
    return render(request,'personal/contact.html')

def lampung(request):
    return render(request,'personal/contact.html')
