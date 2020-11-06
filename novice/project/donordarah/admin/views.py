from django.shortcuts import render
from . import models

def index(req):
    return render(req, 'admin/index.html')