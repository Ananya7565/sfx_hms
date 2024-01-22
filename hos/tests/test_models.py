import datetime
from django.test import TestCase
from hos.models import Department,Patient,Hospital,Visited,Doctor
from datetime import date,timedelta,datetime


class DepartmentModelTest(TestCase):
    
    def setUp(self):
        self.department = Department.objects.create(department_name='Test Department')
        self.patient = Patient.objects.create(patient_name='Test Patient',date_of_birth='2002-01-02' , mobile_number='1111111111' ,gender='female')
        self.hospital = Hospital.objects.create(hospital_name='Test Hospital', address='Test Address')
        self.hospital.department.add(self.department)
        self.doctor = Doctor.objects.create(doctor_name='Test Doctor',department=self.department,hospital=self.hospital)

    def test_department(self):
        new_department = Department.objects.create(department_name='New Department')
        added_department = Department.objects.get(department_name='New Department')
        self.assertEqual(added_department, new_department)
        
    def test_patient(self):
        new_patient = Patient.objects.create(patient_name='AnanyaS' , date_of_birth='2002-01-02' , mobile_number='1111111111' ,gender='female')
        added_patient = Patient.objects.get(patient_name='AnanyaS')
        self.assertEqual(added_patient , new_patient)
    
    def test_hospital(self):
        initial_hos_count = Hospital.objects.count()
        new_hospital_data = Hospital.objects.create(hospital_name= 'Test Hospital',address= 'Test Address')
        new_hospital_data.department.add(self.department)   # for many to many relationships use add
        self.assertEqual(Hospital.objects.count() , initial_hos_count + 1)

    def test_visit(self):
        initial_visited_count = Visited.objects.count()
        visited_data = Visited.objects.create(patient = self.patient, date_and_time=datetime.now() ,hospital=self.hospital , doctor=self.doctor,department=self.department, status='primary check')
        self.assertEqual(Visited.objects.count() , initial_visited_count + 1)
    
    def test_doctor(self):
        initial_doctor_count = Doctor.objects.count()
        doctor_data = Doctor.objects.create(doctor_name='Test Doctor', department=self.department, hospital=self.hospital)
        self.assertEqual(Doctor.objects.count(), initial_doctor_count + 1)
        