
from django.shortcuts import get_object_or_404
from rest_framework import generics,status,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hospital,Department,Patient, Visited , Doctor
#from .serializers import HospitalSerializer,VisitedSerializer,PatientUpdateSerializer,PatientCreateSerializer
from .serializers import HospitalSerializer,VisitedSerializer,PatientCreateSerializer,DepartmentSerializer,DoctorSerializer
from django.http import Http404
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from ast import literal_eval
#patient get not working

'''
class HospitalByNameView(APIView):
    def get(self, request, name, format=None):
        try:
            hospitals = Hospital.objects.filter(name=name)
            print("TTTTTTTTTTTTTTTTTTTTTTTTTt" , hospitals)
            #if not hospitals.exists():          # .exists() return True if the queryset returns any rows
            #raise Http404("Hospital not found")
                #return Response(status)
            #print("not forund")
            
            serializer = HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)
        except:
            return Response(Http404)
'''

# if you give one department you will get all the hospitals which have that department
class HospitalsByDepartmentView(APIView):
    #def get(self, request, department_name, format=None):
    
    def get(self, request,department_id):
        print("This is the department name" , department_id)
        try:
            departmentr = Department.objects.get(id=department_id)
            hospitals = Hospital.objects.filter(department = departmentr)
            #hospitals = department.hospital_set.all()    # department is foreign key in hospital, to get all the departments associated to hospital h we should just do h.department, but to get all the hospitals associated to department 'd' we should do d.hospital_set.all()
            #In the above line you cant use hospital_set because hospital and department have a many to many relationship
            serializer = HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)
        except Department.DoesNotExist:
            print("I am in exception")
            return Response({"error": f"Department '{department_id}' not found"}, status=status.HTTP_404_NOT_FOUND)
    def post(self,request):
        try:
            ser = DepartmentSerializer(data = request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data , status=status.HTTP_201_CREATED)
        except:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,department_id,format=None):
        try:
            dept = Department.objects.get(id = department_id)
            print("This is dept" , dept)
            print("TYPE" ,type(dept))
            #serializer = DepartmentSerializer(dept)
            dept.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            #return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        except:
            #return Response({"error": f"Department'{department_id}' not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response(status)
























class MyHospitalView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    
    #def get(self, request, hospital_name=None, format=None):
    def get(self , request,hospital_name=None , format=None):     # here we set hospital_name to None, because providing the hospital name in the get request is optional, if we want details of all hospitals we give no hospital name , if we want details of 1 hospital we provide the hospital name
        if hospital_name:
            #print("AAAAAAAAAAAAAAA" , request.data)      # this in case of get request will print a {} in console
            #hospital = get_object_or_404(Hospital, name=hospital_name)  # if you want to print just the hospital address do return Response(hospital.address)
            hospital = Hospital.objects.filter(hospital_name = hospital_name)    # if it was hospital = Hospital.objects.filter(name=hospital_name , many = True)   make sure you add many = True when using filter
            #print("hosssssss" , hospital)
            serializer = HospitalSerializer(hospital ,many=True)
            return Response(serializer.data)
        else:
            hospitals = Hospital.objects.all()
            serializer = HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):   ##########here see if it can be def post(self,request)
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():    # when deserializing before putting the data in database you have to check if its valid
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, hospital_id=None, format=None):
        #hospital = get_object_or_404(Hospital, name=hospital_name)
        try:
            hospital = Hospital.objects.get(id=hospital_id)
            print("this is hossss" , hospital)
            serializer = HospitalSerializer(instance=hospital, data=request.data)  #in HospitalSerializer the first argument is the existing data , and the 2nd argument is the data that should be overwritten
            if serializer.is_valid():
                serializer.save()
                print("This is if block")
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            print("Thwefyg  2wwwwwww8y")
            raise Http404
            

    def delete(self, request, hospital_id=None, format=None):
        #hospital = get_object_or_404(Hospital, name=hospital_name)
        try:
            print("i am before the hospital")
            hospital = Hospital.objects.get(id = hospital_id)
            print("This is hos to be deleted" , hospital)
            hospital.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error": f"Hospital '{hospital_id}' not found"}, status=status.HTTP_404_NOT_FOUND)







































class PatientCreateView(APIView):
    def get(self,request,mobile_number=None,*args,**kwargs):
        try:
            print(mobile_number)
            print(type(mobile_number))
            k = literal_eval(mobile_number)
            m = Patient.objects.filter(mobile_number = k)
            print("here")
            serializer = PatientCreateSerializer(m,many=True)
            print(serializer)
            #if(serializer.is_valid()):
             #   print("helooooooooooo")
            return Response(serializer.data)
            #else:
             #   print("i am in elseeeeeee")
              #  return Response({"message":"failed"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": f"Patient with this mobile number  not found"}, status=status.HTTP_404_NOT_FOUND)

    #below function not used can be deleted
   
    def post(self,request,format=None):
        #all_pat = Patient.objects.all()
        
        #mobile_numbers = []                  #dont use list,visit table doctor add, visit add post
        #d = {}
        #for individual_patient_details in all_pat:
         #   mobile_numbers.append(individual_patient_details.mobile_number)
          #  d[individual_patient_details.mobile_number] = individual_patient_details.patient_name

        # print("This is all the patients mobile no" , mobile_numbers)
        # print("This is the dicttttttttt" , d)
        print("this is the request dataaaaaaa" , request.data)
        a = request.data
        print("this is the request data phoneeeeeeeeeeeeeeee" , a['mobile_number'])
        # if(a['mobile_number'] in mobile_numbers):
        #     print("i am in the 1st if loop")
        #     if(a['patient_name'] == d[a['mobile_number']]): 
        #        print("i am in the 2nd if loop")
        #        return Response({"error": f"The number'{a['mobile_number']}' already exists , it belongs to {a['patient_name']}"}, status=500)
        k = a['mobile_number']
        try:
            s = Patient.objects.get(mobile_number = k)
            if(a['patient_name'] == s.patient_name):
                return Response({"error": f"The number'{a['mobile_number']}' already exists , it belongs to {a['patient_name']}"}, status=500)
            else:
                serializer = PatientCreateSerializer(data = request.data)
                if(serializer.is_valid()):    #is_valid() will check the data in json format
                    serializer.save()         # .save() will convert the data from json to object format and then save it in the db
                    print("this is idddddd",serializer.data["id"])
                    c = request.data
                   # self.add_to_visit(serializer.data["id"])
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        except:
            serializer = PatientCreateSerializer(data = request.data)
            if(serializer.is_valid()):    #is_valid() will check the data in json format
                serializer.save()         # .save() will convert the data from json to object format and then save it in the db
                print("this is idddddd",serializer.data["id"])
                c = request.data
                #self.add_to_visit(serializer.data["id"])
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,format=None,patient_id = None):
        print("i am in the put call for patient")
        try:
            #print("This is name and num",patient_name,mobile_number)
            #pat = Patient.objects.get(name=patient_name,mobile_number=mobile_number)
            pat = Patient.objects.get(id = patient_id)
            print("still in try")
            serializer = PatientCreateSerializer(instance=pat , data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                #c = request.data
                #self.add_to_visit(c)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Thwefyg  2wwwwwww8y")
            raise e
    def delete(self,request,patient_id = None):
        try:
            s = Patient.objects.get(id = patient_id)
            s.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error": f"Patient '{patient_id}' not found"}, status=status.HTTP_404_NOT_FOUND)









class Appointment(APIView):
    def post(self,request):
        ser = VisitedSerializer(data = request.data)
        if(ser.is_valid()):
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,appointment_id = None):
        try:
            appoint = Visited.objects.get(id = appointment_id)
            ser = VisitedSerializer(instance=appoint , data=request.data)
            if(ser.is_valid()):
                ser.save()
                return Response(ser.data)
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            print("Thwefyg  2wwwwwww8y")
            raise Http404
    def get(self,request,mobile_number = None,*args,**kwargs):
        try:
            k = literal_eval(mobile_number)
            pat = Patient.objects.get(mobile_number = k)
            p = Visited.objects.filter(patient = pat)
            k = VisitedSerializer(p , many = True)
            return Response(k.data)
            #if(k.is_valid()):
             #   return Response(k.data)   
            #else:
             #   return Response({"message":"failed"}, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            print(e)
            return Response({"error": f"No patient found"}, status=status.HTTP_404_NOT_FOUND)
    def delete(self,request,appointment_id = None):
        try:
            p = Visited.objects.get(id = appointment_id)
            k = VisitedSerializer(p)
            p.delete()
            return Response(k.data)
        except Exception as e:
            #return Response({"error": f"Appointment '{appointment_id}' not found"}, status=status.HTTP_404_NOT_FOUND)
            print("erorrrrr" , e)
            raise e
































#class DoctorView(APIView):
 #   def (self,request,department)


class DoctorsInDept(APIView):
    def get(self,request,department_id):
        try:
            d = Department.objects.get(id = department_id)
            print("this is d" , d)
            k = Doctor.objects.filter(department = d)
            k = DoctorSerializer(k , many = True)
            return Response(k.data)
        except Exception as e:
            print("I am in exception")
            print(e)
            return Response({"error": f"error found"}, status=status.HTTP_404_NOT_FOUND)
    



































##############################
#########################
###########
###################
####################
# class VisitedListView(APIView):
#     def get(self,request,format=None,mobile_number=None):

#         m = Visited.objects.filter(patient__mobile = mobile_number)
#         ser = VisitedSerializer(m)
#         return Response(ser.data)









