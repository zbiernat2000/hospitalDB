from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^doctors/', views.doctors, name="index"),
    path('doctor_create/', views.doctor_form, name='doctor_create'),
    path('doctor_update/<int:id>/', views.doctor_form, name='doctor_update'),
    path('doctors/', views.doctors, name='doctors'),
    path('doctors_delete/<int:id>/', views.doctor_delete, name='doctor_delete')
]
