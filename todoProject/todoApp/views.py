from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from django.core.paginator import Paginator

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('deadline', 'priority')

    # Set up pagination
    paginator = Paginator(tasks, 10)  # 10 tasks per page
    page_number = request.GET.get('page')  # Get the current page number from the URL parameters
    page_obj = paginator.get_page(page_number)  # Get the Page object for the current page

    return render(request, 'todoApp/tasks_list.html', {'page_obj': page_obj})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'todoApp/task_form.html', {'form': form})

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoApp/task_form.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todoApp/delete_task.html', {'task': task})