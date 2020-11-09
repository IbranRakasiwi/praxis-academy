from django.urls import path
from django.contrib import admin
from django.shortcuts import render
from . import views

urlpatterns = [
    path('/donor/',views.index),
    path('/tambah', views.tambah),
    path('<id>/edit', views.edit),
    path('<id>/', views.detail),
    path('<id>/hapus', views.delete),
    
]