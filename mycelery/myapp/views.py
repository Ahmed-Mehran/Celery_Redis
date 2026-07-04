from django.shortcuts import render
from myapp.tasks import add
from celery.result import AsyncResult

# Create your views here.

## Enqueue Task using delay()
def index(request):

    result = add.apply_async(args=[10,20])
    
    return render(request, "myapp/home.html", {'result':result})

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    # print("Ready: ", result.ready())
    # print("Successful: ", result.successful())
    # print("Failed: ", result.failed())
    # print("Get: ", result.get())
    return render(request, 'myapp/result.html', {'result':result})