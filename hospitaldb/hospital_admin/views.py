from django.http import HttpResponse
from django.shortcuts import render

from .models import Doctor

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


#TODO do table to display doctor
def doctors(request):
    doctorlist = Doctor.objects.all()
    context = {'doctorlist': doctorlist}
    return render(request, 'Doctors.html', context)