from django.shortcuts import render
from myapp.tasks import add

# Create your views here.

## Enqueue Task using delay()
def index(request):
    
    print("Results: ")

    result1 = add.apply_async(args=[10,20])
    
    print(result1.id)
    
    return render(request, "myapp/home.html")

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')