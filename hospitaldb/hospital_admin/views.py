from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import DoctorForm
from .models import Doctor


def index(request):
    return render(request, 'index.html')

def doctors(request):
    doctorlist = Doctor.objects.all()
    context = {'doctorlist': doctorlist}
    return render(request, 'doctor/Doctors.html', context)

def doctor_form(request):
    if request.method == "GET":
        form = DoctorForm()
        return render(request, 'doctor/doctor_form.html',{'form':form})
    else:
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("invalid")
        return redirect('/doctors/')