from django.shortcuts import render, redirect
from . task_form import TaskForm
from . models import Task

# Create your views here.
def index(request):
    data = Task.objects.all()
    return render(request, 'index.html', {'data':data})

def create_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        print('debugging1')
        if task_form.is_valid():
            print('debugging2')
            task_form.save()
            return redirect('index')
        
            
    form1 = TaskForm()
    return render(request, 'create_task.html', {'form': form1})


def update_task(request, id):
    task=Task.objects.get(id=id)
    
    if request.method=='POST':
        #update the record with new values
        task_form=TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('index')
    task_form=TaskForm(instance=task)  #An existing object is passed to the Form
    return render(request,'create_task.html',{'form':task_form})  

def delete_task(request, id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect("index")