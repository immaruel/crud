from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import CreateForm

def home(request):
    blogs = Blog.objects.all()
    
    context = {'blogs':blogs}
    return render(request, 'app/home.html',context)

def create(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'app/create.html',context)

def updatePost(request, pk):
    blogs = Blog.objects.get(id=pk)
    form = CreateForm(instance=blog)

    if request.method == 'POST':
        form = CreateForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'app/create.html',context)

def deletePost(request, pk):
    blogs = Blog.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('/')

    context = {'item':blog}
    return render(request, 'app/delete.html',context)