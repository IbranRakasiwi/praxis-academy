from django.shortcuts import render
from . import models

def index(req):
    task = models.Pasien.objects.all()
    return render(req, 'darah/index.html',
    { 'data' : task,
    })

def tambah(req):
    if req.POST:
        models.Pasien.objects.create(
        no_pasien=req.POST['no_pasien'],
        nama_pasien=req.POST['nama_pasien'],
        jenis_kelamin=req.POST['jenis_kelamin'],
        alamat_pasien=req.POST['alamat_pasien'],
        no_hp=req.POST['no_hp'])
        return redirect('darah/index.html')
    task = models.Pasien.objects.all()
    return render(req, 'darah/tambah.html',
    { 'data' : task,
    })

def detail(req, id):
    task = models.Pasien.objects.filter(pk=id).first()
    return render(req, 'darah/detail.html',
    { 'data' : task,
    })

def edit(req, id):
    if req.POST:
        models.Pasien.objects.filter(pk=id).update(
        no_pasien=req.POST['no_pasien'],
        nama_pasien=req.POST['nama_pasien'],
        jenis_kelamin=req.POST['jenis_kelamin'],
        alamat_pasien=req.POST['alamat_pasien'],
        no_hp=req.POST['no_hp'],)
        return redirect('darah/')
    task = models.Online.objects.filter(pk=id).first()
    return render(req, 'dararh/edit.html',
    { 'data' : task,
    })


def delete(req, id):
    task = models.Pasien.objects.filter(pk=id).delete()
    return redirect('darah/')