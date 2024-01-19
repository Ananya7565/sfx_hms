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
        #fields = ['department_id', 'name']
        fields = '__all__'
    #def __str__
    

    
class HospitalSerializer(serializers.ModelSerializer):
      
    #departments = DepartmentSerializer(many=True, read_only=True, source='department_set')
    
    class Meta:
        model = Hospital
        fields = '__all__'
        # fields = ['id', 'name', 'address','departments']
'''
    def create(self, validated_data):
        department_name = validated_data.pop('department_name', None)
        if department_name:
            departments = [Department.objects.get_or_create(name=name)[0] for name in department_name]
        else:
            departments = []
        hospital = Hospital.objects.create(**validated_data)
        hospital.department.set(departments)

        return hospital
        
        '''


'''

class VisitedSerializer(serializers.ModelSerializer):
    patient = serializers.CharField(source='patient.mobile_number')
    hospital = serializers.SerializerMethodField()

    class Meta:
        model = Visited
        fields = ['visited_id', 'patient', 'date_and_time', 'hospital']

    def get_hospital(self, obj):
        return {
            'id': obj.hospital.id,
            'name': obj.hospital.name,
            'address': obj.hospital.address,
            'departments': [department.name for department in obj.hospital.department.all()]
        }
    
'''
class VisitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visited
        fields = '__all__'
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

        # Calculate age based on the provided date of birth
        age = (datetime.date.today() - value).days // 365

        # Validate that the age is less than or equal to 150 and not negative
        if age > 150:
            raise serializers.ValidationError("Date of birth cant make you more than 150")
        if age<0:
            raise serializers.ValidationError("Date if birth cant be a future date")

        return value
    

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    #def validate_mobile_number(mobile_number)

'''
class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('mobile_number',)
'''