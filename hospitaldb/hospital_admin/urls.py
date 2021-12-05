from django.urls import path
from django.conf.urls import url
from . import views

#Unresolved reference issue with admin.site.urls
urlpatterns = [
    path('', views.index, name='index'),
    path('doctor_create/', views.doctor_form, name='doctor_create'),
    path('doctor_update/<int:id>/', views.doctor_form, name='doctor_update'),
    path('doctors/', views.doctors, name='doctors'),
    path('doctors_delete/<int:id>/', views.doctor_delete, name='doctor_delete'),
    path('department/', views.department, name='department'),
    path('department_create/', views.department_form, name='department_create'),
    path('department_update/<int:id>/', views.department_form, name='department_update'),
    path('department_delete/<int:id>/', views.department_delete, name='department_delete'),
    path('department_view/<int:id>/', views.department_view, name='department_view'),
    path('patient/', views.patient, name='patient'),
    path('patient_create/', views.patient_form, name='patient_create'),
    path('patient_update/<int:id>/', views.patient_form, name='patient_update'),
    path('patient_delete/<int:id>/', views.patient_delete, name='patient_delete'),
    path('patient_view/<int:id>/', views.patient_view, name='patient_view'),
    path('appointment/', views.appointment, name='appointment'),
    path('appointment_create/', views.appointment_form, name='appointment_create'),
    path('appointment_update/<int:id>/', views.appointment_form, name='appointment_update'),
    path('appointment_delete/<int:id>/', views.appointment_delete, name='appointment_delete'),
    path('appointment_view/<int:id>/', views.appointment_view, name='appointment_view'),
    path('procedure/', views.procedure, name='procedure'),
    path('procedure_create/', views.procedure_form, name='procedure_create'),
    path('procedure_update/<int:id>/', views.procedure_form, name='procedure_update'),
    path('procedure_delete/<int:id>/', views.procedure_delete, name='procedure_delete'),
    path('procedure_view/<int:id>/', views.procedure_view, name='procedure_view'),
    path('procedureOrder/', views.procedureOrder, name='procedureOrder'),
    path('procedureOrder_create/', views.procedureOrder_form, name='procedureOrder_create'),
    path('procedureOrder_update/<int:id>/', views.procedureOrder_form, name='procedureOrder_update'),
    path('procedureOrder_delete/<int:id>/', views.procedureOrder_delete, name='procedureOrder_delete'),
    path('procedureOrder_view/<int:id>/', views.procedureOrder_view, name='procedureOrder_view'),
]
