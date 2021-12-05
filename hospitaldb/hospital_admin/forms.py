from django import forms

from .models import Doctor
from .models import Department
from .models import Patient
from .models import Appointment


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('departmentID', 'first_name', 'last_name', 'email', 'phone_number', 'pager_number', 'salary')



class AppointmentForm(forms.ModelForm):
   class Meta:
       model = Appointment
       fields = '__all__'
