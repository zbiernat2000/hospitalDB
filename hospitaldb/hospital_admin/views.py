from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DoctorForm, DepartmentForm, PatientForm, AppointmentForm, ProcedureForm, ProcedureOrderForm
from .models import Doctor, Department, Patient, Appointment, Procedure, ProcedureOrder



def index(request):
    return render(request, 'index.html')


def doctors(request):
    doctorlist = Doctor.objects.all()
    context = {'doctorlist': doctorlist}
    return render(request, 'doctor/Doctors.html', context)


def doctor_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DoctorForm()
        else:
            doctor = Doctor.objects.get(pk=id)
            form = DoctorForm(instance=doctor)
        return render(request, 'doctor/doctor_form.html', {'form': form})
    else:
        if id == 0:
            form = DoctorForm(request.POST)
        else:
            doctor = Doctor.objects.get(pk=id)
            form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
        else:
            print("invalid")
        return redirect('/doctors/')


def doctor_delete(request, id):
    doctor = Doctor.objects.get(pk=id)
    doctor.delete()
    return redirect('/doctors/')


def department(request):
    departmentlist = Department.objects.all()
    context = {'departmentlist': departmentlist}
    return render(request, 'department/Department.html', context)


def department_delete(request, id):
    department = Department.objects.get(pk=id)
    department.delete()
    return redirect('/department/')


def department_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DepartmentForm()
        else:
            department = Department.objects.get(pk=id)
            form = DepartmentForm(instance=department)
        return render(request, 'doctor/doctor_form.html', {'form': form})
    else:
        if id == 0:
            form = DepartmentForm(request.POST)
        else:
            department = Department.objects.get(pk=id)
            form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
        else:
            print("invalid")
        return redirect('/department/')


def department_view(request,id):
    department = Department.objects.get(pk=id)
    doctorlist = Doctor.objects.filter(departmentID=id)

    context = {'doctorlist': doctorlist,
               'department': department}
    return render(request, 'department/view_department.html', context)

def patient_view(request,id):
    pass

def patient(request):
   patientlist = Patient.objects.all()
   context = {'patientlist': patientlist}
   return render(request, 'patient/Patient.html', context)


def patient_delete(request, id):
   patient = Patient.objects.get(pk=id)
   patient.delete()
   return redirect('/patient/')


def patient_form(request, id=0):
   if request.method == "GET":
       if id == 0:
           form = PatientForm()
       else:
           patient = Patient.objects.get(pk=id)
           form = PatientForm(instance=patient)
       return render(request, 'doctor/doctor_form.html', {'form': form})
   else:
       if id == 0:
           form = PatientForm(request.POST)
       else:
           patient = Patient.objects.get(pk=id)
           form = PatientForm(request.POST, instance=patient)
       if form.is_valid():
           form.save()
       else:
           print("invalid")
       return redirect('/patient/')

def appointment_view(request,id=0):
    pass

def appointment(request):
   appointmentlist = Appointment.objects.all()
   context = {'appointmentlist': appointmentlist}
   return render(request, 'appointment/Appointment.html', context)


def appointment_delete(request, id):
   appointment = Appointment.objects.get(pk=id)
   appointment.delete()
   return redirect('/appointment/')


def appointment_form(request, id=0):
   if request.method == "GET":
       if id == 0:
           form = AppointmentForm()
       else:
           appointment = Appointment.objects.get(pk=id)
           form = AppointmentForm(instance=appointment)
       return render(request, 'doctor/doctor_form.html', {'form': form})
   else:
       if id == 0:
           form = AppointmentForm(request.POST)
       else:
           appointment = Appointment.objects.get(pk=id)
           form = AppointmentForm(request.POST, instance=appointment)
       if form.is_valid():
           form.save()
       else:
           print("invalid")
       return redirect('/appointment/')

def procedure(request):
   procedurelist = Procedure.objects.all()
   context = {'procedurelist': procedurelist}
   return render(request, 'procedure/Procedure.html', context)


def procedure_delete(request, id):
   procedure = Procedure.objects.get(pk=id)
   procedure.delete()
   return redirect('/procedure/')

def procedure_form(request, id=0):
   if request.method == "GET":
       if id == 0:
           form = ProcedureForm()
       else:
           procedure = Procedure.objects.get(pk=id)
           form = ProcedureForm(instance=procedure)
       return render(request, 'doctor/doctor_form.html', {'form': form})
   else:
       if id == 0:
           form = ProcedureForm(request.POST)
       else:
           procedure = Procedure.objects.get(pk=id)
           form = ProcedureForm(request.POST, instance=procedure)
       if form.is_valid():
           form.save()
       else:
           print("invalid")
       return redirect('/procedure/')

def procedure_view(request,id):
    pass

def procedureOrder(request):
   procedureOrderlist = ProcedureOrder.objects.all()
   context = {'procedureOrderlist': procedureOrderlist}
   return render(request, 'procedureOrder/ProcedureOrder.html', context)


def procedureOrder_delete(request, id):
   procedureOrder = ProcedureOrder.objects.get(pk=id)
   procedureOrder.delete()
   return redirect('/procedureOrder/')


def procedureOrder_form(request, id=0):
   if request.method == "GET":
       if id == 0:
           form = ProcedureOrderForm()
       else:
           procedureOrder = ProcedureOrder.objects.get(pk=id)
           form = ProcedureOrderForm(instance=procedureOrder)
       return render(request, 'doctor/doctor_form.html', {'form': form})
   else:
       if id == 0:
           form = ProcedureOrderForm(request.POST)
       else:
           procedureOrder = ProcedureOrder.objects.get(pk=id)
           form = ProcedureOrderForm(request.POST, instance=procedureOrder)
       if form.is_valid():
           form.save()
       else:
           print("invalid")
       return redirect('/procedureOrder/')


def procedureOrder_view(request,id):
    pass
