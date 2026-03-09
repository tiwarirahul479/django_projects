from django.shortcuts import render
from first_celery_project.celery import add   # import the task from celery.py
from myapp.tasks import sub
from celery.result import AsyncResult

# Create your views here.

# # using apply_async function
# def index(request):
#     print("Index Hit")
#     res = add.apply_async(args=[10, 20])    # enqueue the task to the broker, in my case broker is redis
#     print(f"Index result = {res}")
#     res1 = sub.apply_async(args=[80, 30])
#     print(f"Sub result = {res1}")
#     return render(request, 'index.html')

# # using delay function
# def index(request):
#     print("Index Hit")
#     res = add.delay(10, 20)    # enqueue the task to the broker, in my case broker is redis
#     print(f"Index result = {res}")
#     res1 = sub.delay(80, 30)
#     print(f"Sub result = {res1}")
#     return render(request, 'index.html')

def index(request):
    result = add.delay(10, 20)
    return render(request, 'index.html', {'result': result})

def about(request):
    print("About Hit")
    return render(request, 'about.html')

def contact(request):
    print("Contact Hit")
    return render(request, 'contact.html')

def check_result(request, task_id):
    result = AsyncResult(task_id)
    # result.ready()     # when result is ready, return True
    # result.successful()   # when result is success, return True
    # result.failed()   # when result is failed, return True
    return render(request, 'check_result.html', {'result': result})
