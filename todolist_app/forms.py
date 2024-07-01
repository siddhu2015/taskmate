from todolist_app.models import Tasklist
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model= Tasklist
        fields=['task','done']