from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def details(request):
    return render(request, "blog_details.html")

def contact(request):
    return render(request, "contact.html")

def about_us(request):
    return render(request, "about.html")

def elements(request):
    return render(request, "elements.html")

def help(request):
    return render(request, "help.html")

def packages(request):
    return render(request, "packages.html")

def services(request):
    return render(request, "services.html")

def credentials(request):
    return render(request, "login.html")