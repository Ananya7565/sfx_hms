# serializers.py
from rest_framework import serializers
from .models import Hospital,Department,Patient,Visited


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



class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'



'''
class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('mobile_number',)
'''