#from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models


def index(req):
    task = models.Online.objects.all()
    return render(req, 'pembeli/index.html',
    { 'data' : task,
    })


def tambah(req):
    if req.POST:
        models.Online.objects.create(
        nama_barang=req.POST['nama_barang'],
        ukuran_barang=req.POST['ukuran_barang'],
        nama_pemesan=req.POST['nama_pemesan'],
        alamat_pemesan=req.POST['alamat_pemesan'],
        jumlah_pemesanan=req.POST['jumlah_pemesanan'],)
        return redirect('/pembeli/')
    task = models.Online.objects.all()
    return render(req, 'pembeli/tambah.html',
    { 'data' : task,
    })

def detail(req, id):
    task = models.Online.objects.filter(pk=id).first()
    return render(req, 'pembeli/detail.html',
    { 'data' : task,
    })

def edit(req, id):
    if req.POST:
        models.Online.objects.filter(pk=id).update(
        nama_barang=req.POST['nama_barang'],
        ukuran_barang=req.POST['ukuran_barang'],
        nama_pemesan=req.POST['nama_pemesan'],
        alamat_pemesan=req.POST['alamat_pemesan'],
        jumlah_pemesanan=req.POST['jumlah_pemesanan'])
        return redirect('/pembeli/')
    task = models.Online.objects.filter(pk=id).first()
    return render(req, 'pembeli/edit.html',
    { 'data' : task,
    })


def delete(req, id):
    task = models.Online.objects.filter(pk=id).delete()
    return redirect('/pembeli/')