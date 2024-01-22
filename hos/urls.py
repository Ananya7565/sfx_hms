from django.urls import path
from . import views
from .views import MyHospitalView,HospitalsByDepartmentView,PatientCreateView,Appointment,DoctorsInDept
app_name = 'hos'
urlpatterns = [

    # DEPARTMENT URLS
    path('api/hospitals_by_department/<int:department_id>/', HospitalsByDepartmentView.as_view(), name='get_hospitals_of_this_dept'),
    # in the above url you are passing str:department_name , so in the function definition the argument has to be department_name only
    path('api/hospitals_by_department/' , HospitalsByDepartmentView.as_view() , name = 'create_dept'),
    path('api/hospitals_by_department/<int:department_id>/' , HospitalsByDepartmentView.as_view() , name='delete dept'),

    # HOSPITAL URLS
    path('api/hospitals/', MyHospitalView.as_view(), name='api_create_hospital'),
    path('api/hospitals/<int:hospital_id>/', MyHospitalView.as_view(), name='api_update_hospital'),
    path('api/hospitals/<int:hospital_id>/', MyHospitalView.as_view(), name='api_delete_hospital'),
    path('hos_all/', MyHospitalView.as_view(), name='hospital-list'),
    path('hos_all/<str:hospital_name>/' , MyHospitalView.as_view() , name='indi_hos'),
    
    # PATIENT URLS
    path('patients/', PatientCreateView.as_view(), name='patient-create'),
    path('patients/<int:patient_id>/' , PatientCreateView.as_view() , name='update pat'),
    path('patients/<int:patient_id>/' , PatientCreateView.as_view() , name='delete-patient'),
    path('patients/<str:mobile_number>/' , PatientCreateView.as_view() , name='patient-get-mobile_number'),

    # APPOINTMENT URLS
    path('appointment/' ,Appointment.as_view() , name='create-appointment'),
    path('appointment/<int:appointment_id>/' , Appointment.as_view() , name='update-appointment'),
    path('appointment/<int:appointment_id>/' , Appointment.as_view() , name='delete-appointment'),
    path('appointment/<str:mobile_number>/' , Appointment.as_view() , name='get-appointment'),

    # DOCTOR URLS
    path('doc/<int:department_id>/' , DoctorsInDept.as_view() , name='get-doctors-in-dept'),

]

'''

###############################################################   DEPARTMENT URLS    ##################################################
GET  -   gets list of hospitals with department id 2
http://localhost:8000/hos/api/hospitals_by_department/2/


POST -  creates a new department
http://localhost:8000/hos/api/hospitals_by_department/
REQUEST BODY
{
    "department_name" : "motherhood"
}

DELETE - deletes department of id 7
http://localhost:8000/hos/api/hospitals_by_department/7/


################################################################   HOSPITAL URLS      ###################################################
POST - creates a new hospital
http://localhost:8000/hos/api/hospitals/
REQUEST BODY
{
    "hospital_name" : "Ananya_hos",
    "address" : "Ananya Road",
    "department" : [5]
}


PUT - Updates details of hospital id 11
http://localhost:8000/hos/api/hospitals/11/
REQUEST BODY
{
    "hospital_name" : "Ananya_hos",
    "address" : "Ananya New Road",
    "department" : [5]
}


DELETE - Deletes hospital of id 11
http://localhost:8000/hos/api/hospitals/11/

GET - gets a list of all the hospitals
http://localhost:8000/hos/hos_all/

GET - gets the details of all hospitals with name q_hos
http://localhost:8000/hos/hos_all/q_hos/


###################################################################   PATIENT URLS       ##################################################
POST - Creates a new patient
http://localhost:8000/hos/patients/
REQUEST BODY 
{
    "patient_name" : "Ananya",
    "date_of_birth" : "2002-01-02",
    "mobile_number" : "9686454642" ,
    "gender" : "female"
}

PUT - Updates patient with id 26
http://localhost:8000/hos/patients/26/
REQUEST BODY
{
    "patient_name" : "Ananya",
    "date_of_birth" : "2002-11-02",
    "mobile_number" : "9686454642" ,
    "gender" : "female"
}

GET - gets patient with mobile number 9686454642
http://localhost:8000/hos/patients/"9686454642"/

DELETE - deletes patient with id 26
http://localhost:8000/hos/patients/26/


###################################################################  APPOINTMENT URLS     #################################################
POST - create a new appointment
http://localhost:8000/hos/appointment/
REQUEST BODY 
{
    "patient" : 1,
    "date_and_time" : "2024-01-20 11:30:32.927588",
    "hospital" : 1,
    "doctor" : 1,
    "department" : 2,
    "status" : "primary check"
}

PUT - only the date and time field of appointment id 17 can be updated
http://localhost:8000/hos/appointment/17/
REQUEST BODY
{
    "patient" : 2,
    "date_and_time" : "2024-01-22 11:30:32.927588",
    "hospital" : 1,
    "doctor" : 1,
    "department" : 2,
    "status" : "secondary check"
}

GET - gets appointment history of patient with mobile number 6666666665
http://localhost:8000/hos/appointment/"6666666665"/

DELETE - deletes appointment with id 9
http://localhost:8000/hos/appointment/9/


###################################################################    DOCTOR URLS       ##################################################
GET  -  gets list of doctors with department id 2
http://localhost:8000/hos/doc/2/


'''