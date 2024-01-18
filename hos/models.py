from django.db import models
from django.core.validators import RegexValidator

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    #department_id = models.AutoField(primary_key=True)     # this line is changed
    def __str__(self):
        return self.name
    
class Hospital(models.Model):
    name = models.CharField(max_length = 90)
    address = models.CharField(max_length = 90)
    department = models.ManyToManyField(Department)
    def __str__(self):
        return f"{self.name}"



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
    STATUS_CHOICES = [
        ('admitted' , 'Admitted'),
        ('release' , 'Release'),
        ('primary check' , 'Primary Check'),
        ('secondary check' , 'Secondary Check'),
    ]

    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    #mobile_number = models.CharField(max_length=10, primary_key=True , unique = True) ###########check this 
    mobile_number = models.CharField(max_length=10 , verbose_name="Phone number" , unique = True , validators=[phone_number_validator])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    doctor_name = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    #primary id not phone
class Visited(models.Model):
    #visited_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(auto_now_add=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True)

    
