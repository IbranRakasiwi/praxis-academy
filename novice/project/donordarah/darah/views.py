from django.shortcuts import render, redirect
from . import models

def index(req):
    task = models.Pasien.objects.all()
    return render(req, 'darah/index.html', 
    { 'data' : task,}
    )


def tambah(req):
    if req.POST:
        models.Pasien.objects.create(
        no_pasien=req.POST['no_pasien'],
        nama_pasien=req.POST['nama_pasien'],
        jenis_kelamin=req.POST['jenis_kelamin'],
        alamat_pasien=req.POST['alamat_pasien'],
        no_hp=req.POST['no_hp'])
        return redirect('list-darah')
    task = models.Pasien.objects.all()
    return render(req, 'darah/tambah.html')
    