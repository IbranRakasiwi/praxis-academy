from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('<id>/', views.detail),
    path('<id>/edit', views.edit),
]