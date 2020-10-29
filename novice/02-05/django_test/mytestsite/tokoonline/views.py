#from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


def index(req):
    task = models.Online.objects.all()
    return render(req, 'task/index.html',
    { 'data' : task,
    })


def tambah(req):
    if req.POST:
        models.Online.objects.create(
        nomor_id=req.POST['id'],
        nama_barang=req.POST['nama_barang'],
        ukuran=req.POST['ukuran'],
        nama_pemesan=req.POST['nama_pemesan'],
        alamat_pemesan=req.POST['alamat'])
        return redirect('/')
    task = models.Online.objects.all()
    return render(req, 'task/tambah.html',
    { 'data' : task,
    })

def detail(req, id):
    task = models.Online.objects.filter(pk=id).first()
    return render(req, 'task/detail.html',
    { 'data' : task,
    })

def edit(req, id):
    if req.POST:
        models.Online.objects.filter(pk=id).update(
        nomor_id=req.POST['id'],
        nama_barang=req.POST['nama_barang'],
        ukuran=req.POST['ukuran'],
        nama_pemesan=req.POST['nama_pemesan'],
        alamat_pemesan=req.POST['alamat_pemesam'])
        return redirect('/')
    task = models.Online.objects.filter(pk=id).first()
    return render(req, 'task/edit.html',
    { 'data' : task,
    })


def delete(req, id):
    task = models.Online.objects.filter(pk=id).delete()
    return redirect('/')