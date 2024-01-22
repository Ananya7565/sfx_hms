# serializers.py
import datetime
from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Hospital,Department,Patient,Visited,Doctor
from django.utils import timezone
from rest_framework.response import Response

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
    
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
        
class VisitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visited
        fields = '__all__'
        # here i am allowing the user to be able t update only appointment date
        read_only_fields = ('patient', 'hospital' , 'doctor' , 'department' , 'status' , )
    def validate_date_and_time(self, value):         # the functio name has to be validat_<field_name>
        # Here i am validating the date and time fields 
        if value < timezone.now():
            raise serializers.ValidationError("Appointment date must be in the future.")
        max_allowed_date = timezone.now() + datetime.timedelta(weeks=2)
        if value > max_allowed_date:
            raise serializers.ValidationError("Appointment date must be within the next 2 weeks.")
        return value

class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
    def validate_date_of_birth(self,value):
        if isinstance(value, str):
            value = datetime.strptime(value, '%Y-%m-%d').date()
        # Here i am calculating the age based on date of birth
        age = (datetime.date.today() - value).days // 365
        # Here i am making sure that the age is not above 150 or below 0
        if age > 150:
            raise serializers.ValidationError("Date of birth cant make you more than 150")
        if age<0:
            raise serializers.ValidationError("Date if birth cant be a future date")
        return value

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    