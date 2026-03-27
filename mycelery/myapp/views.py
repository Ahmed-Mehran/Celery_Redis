from django.shortcuts import render

# Create your views here.

def index(request):
    
    print("Results: ")
    
    return render(request, "myapp/home.html")

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')