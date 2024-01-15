from django.urls import path
from . import views
from .views import MyHospitalView,HospitalByNameView,HospitalsByDepartmentView,PatientCreateView, VisitedListView , PatientUpdateView

app_name = 'hos'
urlpatterns = [
    
    path('api/hospitals_by_department/<str:department_name>/', HospitalsByDepartmentView.as_view(), name='api_hospitals_by_department'),
    




    
    path('api/hospitals/', MyHospitalView.as_view(), name='api_create_hospital'),
    path('api/hospitals/<str:hospital_name>/', MyHospitalView.as_view(), name='api_update_hospital'),
    path('api/hospitals/<str:hospital_name>/', MyHospitalView.as_view(), name='api_delete_hospital'),
    path('hos_all/', MyHospitalView.as_view(), name='hospital-list'),
    
    






    
    path('patients/', PatientCreateView.as_view(), name='patient-create'),
    path('visited/<str:mobile_number>/', VisitedListView.as_view(), name='visited-list'),
    path('patients/<str:mobile_number>/', PatientUpdateView.as_view(), name='patient-update'),

]








#http://127.0.0.1:8000/hos/api/hospitals_by_name/skin_hos/  ------------------------->  
#[{"id":1,"name":"skin_hos","address":"road","department":{"id":1,"name":"skin"}},{"id":2,"name":"skin_hos","address":"road","department":{"id":2,"name":"heart"}}]
#http://127.0.0.1:8000/hos/api/hospitals_by_department/leg/
#[{"id":3,"name":"leg_hos","address":"qwe_road","department":{"id":3,"name":"leg"}},{"id":4,"name":"new_leg_hos","address":"new_leg_road","department":{"id":3,"name":"leg"}}]
#http://127.0.0.1:8000/hos/hos_all/
#returns details of all the hospitals
#for post, as in creating new hospital with post 
#put this in postman url http://localhost:8000/hos/api/hospitals/
'''
put this in body
{
    "name": "New new Hospital",
    "address": "123 new Main Street",
    "department_name": "heart"
}
'''
#for put as in update a hospital 
#put this in postman http://localhost:8000/hos/api/hospitals/New new Hospital/    ----------here New new Hospital is the name of hospital we want to update
'''
put this in request body

you can change the name,address or department
{
    "name": "new new new new",
    "address": "new add",
    "department_name": "leg" 
}
suppose i add a dept which doesnt exist ill get error 
'''
# for delete if you put hti sin postman url http://localhost:8000/hos/api/hospitals/new new new new/
#it will delete hospital new new new new





#if you use the below api post call a new patient is created
#http://localhost:8000/hos/patients/
#below is example body
'''
{
    "name": "John Doe",
    "date_of_birth": "1990-01-01",
    "mobile_number": "1234567890",
    "gender": "male",
    "doctor_name": "Dr. Smith",
    "hospital":3,
    "status": "admitted"
}
'''

#when you put the below api in chrome url you get visited details of patient 
# http://localhost:8000/hos/visited/1234567890/
# this is the output 
# [{"visited_id":1,"date_and_time":"2024-01-10T11:50:10.426309Z","patient":"1234567890"},{"visited_id":2,"date_and_time":"2024-01-10T11:50:10.439314Z","patient":"1234567890"}]
#if u put this in postman put http://localhost:8000/hos/patients/1234567890/
'''
{
   "name": "Doe",
    "date_of_birth": "1990-01-01",
    "mobile_number": "1234567890",
    "gender": "male",
    "doctor_name": "Dr. Smith",
    "hospital":3,
    "status": "admitted"
}
'''
#then entry is added to visited table not patient. patient is updated