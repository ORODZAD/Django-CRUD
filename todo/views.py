from django.shortcuts import render, redirect
from .models import task


def index(request):
    obj = task.objects.all()
    return render(request, 'todo.html', {'Users': obj})


def create(request):
    name = request.POST.get['name']
    description = request.POST.get['description']
    date_time = request.POST.get['date_time']
    id = None
    obj = task(id, name, description, date_time)
    obj.save
    return redirect('/reg')


def update(request, id):
    data = task.objects.get(id=id)
    return render(request, '/edit.html', {'ex': data})


def delete(request, id):
    data = task.objects.get(id=id)
    data.delete()
    return redirect('/reg')


def edit(request, id):
    description = request.POST.get['description']
    date_time = request.POSt.get['date_time']
    data = task.objects.get(id=id)
    data.name = name
    data.description = description
    data.data_time = date_time
    data.save()
    return redirect('/reg')
