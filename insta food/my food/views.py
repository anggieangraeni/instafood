from django.shortcuts import render

def index(request):
    return render(request,'landing2/template.html')

def about(request):
    return render(request,'landing2/about.html')

def login(request):
    return render(request,'landing2/form.html')

def menu(request):
    return render(request,'landing2/menu.html')

def catering(request):
    return render(request,'landing2/catering.html')

def contact(request):
    return render(request,'landing2/contact.html')
