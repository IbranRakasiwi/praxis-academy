#from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


def index(req):
    task = models.Online.objects.all()
    return render(req, 'barang/index.html',
    { 'data' : task,
    })


def tambah(req):
    if req.POST:
        models.Online.objects.create(
        nama_barang=req.POST['nama_barang'],
        ukuran_barang=req.POST['ukuran_barang'],
        nama_toko=req.POST['nama_toko'],
        jumlah_barang=req.POST['jumlah_barang'],
        )
        return redirect('/barang/')
    task = models.Online.objects.all()
    return render(req, 'barang/tambah.html',
    { 'data' : task,
    })

def detail(req, id):
    task = models.Online.objects.filter(pk=id).first()
    return render(req, 'barang/detail.html',
    { 'data' : task,
    })

def edit(req, id):
    if req.POST:
        models.Online.objects.filter(pk=id).update(
        nama_barang=req.POST['nama_barang'],
        ukuran_barang=req.POST['ukuran_barang'],
        nama_toko=req.POST['nama_toko'],
        jumlah_barang=req.POST['jumlah_barang'])
        return redirect('/barang/')
    task = models.Online.objects.filter(pk=id).first()
    return render(req, 'barang/edit.html',
    { 'data' : task,
    })


def delete(req, id):
    task = models.Online.objects.filter(pk=id).delete()
    return redirect('/barang/')