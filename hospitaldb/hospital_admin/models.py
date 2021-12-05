from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Department(models.Model):
    departmentID = models.AutoField(primary_key=True)
    departmentName = models.CharField(max_length=100)
    budget = models.PositiveIntegerField()
    size = models.PositiveIntegerField()


class Doctor(models.Model):
    doctorID = models.AutoField(primary_key=True)
    departmentID = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=320)
    phone_number = models.BigIntegerField(validators=[MinValueValidator(1000000000),
                                                           MaxValueValidator(9999999999)])
    pager_number = models.BigIntegerField(validators=[MinValueValidator(1000000000),
                                                           MaxValueValidator(9999999999)])
    salary = models.PositiveIntegerField()


class Patient(models.Model):
    patientID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)
    phone_number = models.BigIntegerField(validators=[MinValueValidator(1000000000),
                                                           MaxValueValidator(9999999999)])


class Appointment(models.Model):
    appointmentID = models.AutoField(primary_key=True)
    doctorID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patientID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.CharField(max_length=10)


class Procedure(models.Model):
    procedureID = models.AutoField(primary_key=True)
    procedure_name = models.CharField(max_length=100)


class ProcedureOrder(models.Model):
    procedure_orderID = models.AutoField(primary_key=True)
    appointmentID = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    procedureID = models.ForeignKey(Procedure, on_delete=models.CASCADE)