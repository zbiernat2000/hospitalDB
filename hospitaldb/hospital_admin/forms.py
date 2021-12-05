from django import forms

from .models import Doctor
from .models import Department
from .models import Patient
from .models import Appointment
from .models import Procedure
from .models import ProcedureOrder



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


class ProcedureForm(forms.ModelForm):
   class Meta:
       model = Procedure
       fields = '__all__'


class ProcedureOrderForm(forms.ModelForm):
   class Meta:
       model = ProcedureOrder
       fields = '__all__'

