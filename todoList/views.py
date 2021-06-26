from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('homepage'))
  else:
    form = TaskForm()

  task_list = reversed(Task.objects.all())

  context = {'task_list': task_list, 'form': form}
  return render(request, 'index.html', context)

def update_task(request, pk):
  task = Task.objects.get(id=pk)
  if request.method == 'POST':
    form = TaskForm(request.POST, instance=task)
    if  form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('homepage'))
  else:
    form = TaskForm(instance=task)
  context = {'form': form}
  return render(request, 'update.html', context)

def delete_task(request, pk):
  task = Task.objects.get(id=pk)
  task.delete()

  return HttpResponseRedirect(reverse('homepage'))
