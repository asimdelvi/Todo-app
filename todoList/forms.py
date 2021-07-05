from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = '__all__'
    widgets = {
      'title' : forms.TextInput(attrs={'placeholder': 'Add Task', 'class' : 'form-control'})
    }
