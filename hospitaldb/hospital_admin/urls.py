from django.urls import path
from django.conf.urls import url
from . import views

#Unresolved reference issue with admin.site.urls
urlpatterns = [
    path('', views.index, name='index'),
    url(r'^doctors/', views.doctors, name="index"),
    path('doctor_form/', views.doctor_form, name='doctor_form'),
    path('doctors/', views.doctors, name='doctors')
]
