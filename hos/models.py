from django.db import models
from django.core.validators import RegexValidator
from datetime import date,timedelta

class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.department_name
    
class Hospital(models.Model):
    hospital_name = models.CharField(max_length = 90)
    address = models.CharField(max_length = 90)
    department = models.ManyToManyField(Department)
    def __str__(self):
        return f"{self.hospital_name}"

class Patient(models.Model):
    phone_number_validator = RegexValidator(
        regex=r'^[1-9]\d{9}$',
        message='The phone number you are providing is invalid make sure it is atleast 10 digits and doesnt start with 0'
    )

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
   

    patient_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=10  , validators=[phone_number_validator])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    created_date_time = models.DateTimeField(auto_now_add=True)
    #doctor_name = models.CharField(max_length=255)
   # hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
   # status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    #primary id not phone
    def __str__(self):
        return f"{self.patient_name}"
    
class Doctor(models.Model):
    doctor_name = models.CharField(max_length = 255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital , on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.doctor_name}"
    
class Visited(models.Model):
    #visited_id = models.AutoField(primary_key=True)
    STATUS_CHOICES = [
        ('admitted' , 'Admitted'),
        ('release' , 'Release'),
        ('primary check' , 'Primary Check'),
        ('secondary check' , 'Secondary Check'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True)  #if hospital is deleted all the entries with that hospital are also deleted. blank=true means in forms this field is allowed to be emoty when validating a form
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE )
    department = models.ForeignKey(Department , on_delete = models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES )





    
