from django import forms

from .models import Doctor
from .models import Department




class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('departmentID', 'first_name', 'last_name', 'email', 'phone_number', 'pager_number', 'salary')


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'