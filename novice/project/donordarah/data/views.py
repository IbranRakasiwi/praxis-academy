from django.shortcuts import render
from . import models

def index(req):
    return render(req, 'data/index.html')