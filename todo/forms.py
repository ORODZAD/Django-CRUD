from datetime import datetime
from django import forms
from .models import task

class taskForm(forms.ModelForm):
    
    class meta:
        model = task
        fields = ['name', 'description', 'datetime']
        
        