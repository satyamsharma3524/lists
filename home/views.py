from home.models import Tasks,Contacts
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    return render(request,'index.html')

def tasks(request):
    context = {'success':False}
    if request.method == 'POST':
        name = request.POST.get('taskname')
        desc = request.POST.get('taskdesc')
        task = Tasks(Task_name=name,Task_desc=desc,timing=datetime.now())
        task.save()
        context = {'success':True}
    return render(request,'tasks.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    context = {'success':False}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        desc = request.POST.get('desc')
        contact = Contacts(name=name,email=email,contact=contact,desc=desc)
        contact.save()
        context = {'success':True}
    return render(request,'contact.html',context)

def viewtask(request):
    allTasks = Tasks.objects.all()
    context = {'Tasks':allTasks}
    return render(request,'viewtask.html',context)