# mappings/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

class MappingListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.all()
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PatientDoctorMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientMappingsAndDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=id)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)
    def delete(self, request, id):
        try:
            mapping = PatientDoctorMapping.objects.get(id=id)
        except PatientDoctorMapping.DoesNotExist:
            return Response({"detail": "Mapping not found."}, status=status.HTTP_404_NOT_FOUND)

        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



