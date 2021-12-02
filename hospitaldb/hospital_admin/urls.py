from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^doctors/', views.doctors, name="index"),
    path('docotors/', views.doctors, name='doctors')
]