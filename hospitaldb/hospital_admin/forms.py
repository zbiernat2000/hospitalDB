from django import forms


from hospitaldb.hospital_admin.models import Department, Doctor, Patient, Appointment, Procedure, ProcudreOrder

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
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
        model = ProcudreOrder
        fields = '__all__'
