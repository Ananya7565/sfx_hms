from django.test import TestCase
from hos.models import Department,Patient,Hospital,Visited

class DepartmentModelTest(TestCase):
    def test_department(self):
        new_department = Department.objects.create(name='New Department')
        added_department = Department.objects.get(name='New Department')
        self.assertEqual(added_department, new_department)
        
    def test_patient(self):
        new_hospital = Hospital.objects.create(id=34 , name='new test hospital' , address='test road')
        new_patient = Patient.objects.create(name='AnanyaS' , date_of_birth='1990-12-22' , mobile_number='121212' ,
                                             gender='female' , doctor_name='Dr.may' , hospital_id=34 , status='admitted')
        added_patient = Patient.objects.get(name='AnanyaS')
        self.assertEqual(added_patient , new_patient)
    
    def test_hospital(self):
        new_hospital = Hospital.objects.create(id=35 , name='new test hospital' , address='test road')
        added_hospital = Hospital.objects.get(id=35)
        self.assertEqual(new_hospital,added_hospital)    

    def test_visit(self):
        new_hospital = Hospital.objects.create(id=36 , name='new test hospital' , address='test road')
        new_patient = Patient.objects.create(name='AnanyaS' , date_of_birth='1990-12-22' , mobile_number='444' ,
                                             gender='female' , doctor_name='Dr.may' , hospital_id=36 , status='admitted')
        new_visit = Visited.objects.create(date_and_time='2024-01-11 13:06:24.325015' , patient_id=444 , visited_id=4 , hospital_id=36)
        added_visit = Visited.objects.get(visited_id=4)
        self.assertEqual(new_visit , added_visit)