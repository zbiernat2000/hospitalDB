from django import forms

from .models import Doctor
from .models import Department




class DoctorForm(forms.ModelForm):
   # deparment = forms.SlugRelatedField(slug_field="departmentName", queryset= Department.objects.all())

    class Meta:
        model = Doctor
        fields = ('departmentID', 'first_name', 'last_name', 'email', 'phone_number', 'pager_number', 'salary')