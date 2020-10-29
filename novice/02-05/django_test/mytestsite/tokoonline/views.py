#from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Online


def index(request):
    contexs = {
        'toko': Online.objects.all()
    }
    return render(request, 'tamplite.html', contexs)

def detail(request, id):
    task = models.Online.objects.filter(pk=id).first()
    return render(request, 'task/detail.html',
    { 'toko' : task,
    })

def edit(request, id):
    task = models.Online.objects.filter(pk=id).first()
    return render(request, 'task/detail.html',
    { 'toko' : task,
    })

