from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    department_id = models.AutoField(primary_key=True)     # this line is changed
    def __str__(self):
        return self.name
    


    
class Hospital(models.Model):
    name = models.CharField(max_length = 90)
    address = models.CharField(max_length = 90)
    department = models.ManyToManyField(Department)
    def __str__(self):
        return f"{self.name}"



class Patient(models.Model):
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
    mobile_number = models.CharField(max_length=10, primary_key=True , unique = True) ###########check this 
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    doctor_name = models.CharField(max_length=255)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    
class Visited(models.Model):
    visited_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(auto_now_add=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True)

    
