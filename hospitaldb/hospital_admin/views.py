from django.http import HttpResponse


from django.shortcuts import render, redirect

from hospitaldb.hospital_admin.forms import DepartmentForm
from hospitaldb.hospital_admin.models import Department
from hospitaldb.hospital_admin.models import DoctorForm
from hospitaldb.hospital_admin.models import Doctor
from hospitaldb.hospital_admin.models import PatientForm
from hospitaldb.hospital_admin.models import Patient
from hospitaldb.hospital_admin.models import AppointmentForm
from hospitaldb.hospital_admin.models import Appointment
from hospitaldb.hospital_admin.models import ProcedureForm
from hospitaldb.hospital_admin.models import Procedure
from hospitaldb.hospital_admin.models import ProcedureOrderForm
from hospitaldb.hospital_admin.models import ProcedureOrder

def emp(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass #placeholder
            else:
                form = DepartmentForm()
        return render(request, 'hospital_admin/department.html', {'form': form})
    def show(request):
        departments = Department.objects.all()
        return render(request, 'hospital_admin/department.html', {'departments': departments})
    def edit(request, id):
        department = Department.objects.get(id=id)
        return render(request, 'hospital_admin/edit_department.html', {'department': department})
    def update(request, id):
        department = Department.objects.get(id=id)
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('/show')
        return render(request, 'hospital_admin/edit_department.html', {'department': department})
    def delete(request, id):
        department = Department.objects.get(id=id)
        department.delete()
        return redirect('/show')

    # Test above first


