from msilib.schema import CheckBox
from time import time
from unicodedata import name
from xmlrpc.client import boolean
from django.db import models

class task(models.Model):
    name = models.CharField(blank=False,max_length=20)
    description = models.TextField(blank=False,max_length=50)
    complete = models.BooleanField(default=False)
    date_time = models.DateTimeField(auto_now_add=True)
    
    
def __str__(self):
    return self.title
