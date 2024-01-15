
from django.shortcuts import get_object_or_404
from rest_framework import generics,status,serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hospital,Department,Patient, Visited
from .serializers import HospitalSerializer,VisitedSerializer,PatientUpdateSerializer,PatientCreateSerializer
from django.http import Http404
from django.utils import timezone
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated































class HospitalByNameView(APIView):
    def get(self, request, name, format=None):
        hospitals = Hospital.objects.filter(name=name)
        if not hospitals.exists():
            #raise Http404("Hospital not found")
            print("not forund")
            
        serializer = HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)




















# if you give one department you will get all the hospitals which have that department
class HospitalsByDepartmentView(APIView):
    def get(self, request, department_name, format=None):
        try:
            department = Department.objects.get(name=department_name)
            hospitals = department.hospital_set.all()
            serializer = HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)
        except Department.DoesNotExist:
            return Response({"error": f"Department '{department_name}' not found"}, status=status.HTTP_404_NOT_FOUND)
        

class MyHospitalView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, hospital_name=None, format=None):
        if hospital_name:
            hospital = get_object_or_404(Hospital, name=hospital_name)  # if you want to print just the hospital address do return Response(hospital.address)
            serializer = HospitalSerializer(hospital)
            return Response(serializer.data)
        else:
            hospitals = Hospital.objects.all()
            serializer = HospitalSerializer(hospitals, many=True)
            return Response(serializer.data)

    def post(self, request, hospital_name=None, format=None):   ##########here see if it can be def post(self,request)
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, hospital_name=None, format=None):
        hospital = get_object_or_404(Hospital, name=hospital_name)
        serializer = HospitalSerializer(hospital, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, hospital_name=None, format=None):
        hospital = get_object_or_404(Hospital, name=hospital_name)
        hospital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VisitedListView(generics.ListAPIView):     # class name should be model_name.ListView
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Visited.objects.all()
    serializer_class = VisitedSerializer

    def get_queryset(self):
        mobile_number = self.kwargs['mobile_number']
        return Visited.objects.filter(patient__mobile_number=mobile_number)
    




class PatientCreateView(generics.CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer

    def perform_create(self, serializer):
        mobile_number = serializer.validated_data['mobile_number']
        try:
            existing_patient = Patient.objects.get(mobile_number=mobile_number)
            serializer.update(existing_patient, serializer.validated_data)
            patient_instance = existing_patient
        except Patient.DoesNotExist:
            patient_instance = serializer.save()

        hospital_id = self.request.data.get('hospital')
        Visited.objects.create(patient=patient_instance, hospital_id=hospital_id, date_and_time=timezone.now())


class PatientUpdateView(generics.UpdateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientUpdateSerializer
    lookup_field = 'mobile_number'

    def perform_update(self, serializer):
        hospital_id = self.request.data.get('hospital')
        serializer.save()
        updated_patient = serializer.instance
        Visited.objects.create(patient=updated_patient, hospital_id=hospital_id, date_and_time=timezone.now())

