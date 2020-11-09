from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('',views.index, name='list-darah'),
    path('tambah/', views.tambah, name='tambah'),
]