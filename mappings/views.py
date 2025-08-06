from rest_framework import permissions
from .models import PatientDoctorMapping
from patients.models import Patients
from .serializers import PatientDoctorMappingSerializer
from doctors.serializers import DoctorSerializer
from rest_framework.exceptions import PermissionDenied
from doctors.models import Doctors

from rest_framework import generics
class MappingListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PatientDoctorMappingSerializer

    def get_queryset(self):
        return PatientDoctorMapping.objects.all()

    def perform_create(self, serializer):
        patient = serializer.validated_data['patient']
        if patient.creator != self.request.user:
            raise PermissionDenied("You do not have permission to assign doctors to this patient.")
        serializer.save()


class PatientMappingsView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DoctorSerializer

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']

        try:
            patient = Patients.objects.get(id=patient_id)
        except Patients.DoesNotExist:
            return Doctors.objects.none()

        if patient.creator != self.request.user:
            raise PermissionDenied("You do not have permission to view doctors for this patient.")

        doctor_ids = PatientDoctorMapping.objects.filter(
            patient=patient
        ).values_list('doctor_id', flat=True)

        return Doctors.objects.filter(id__in=doctor_ids)


class MappingDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = PatientDoctorMapping.objects.all()
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        mapping = self.get_object()
        if mapping.patient.creator != request.user:
            raise PermissionDenied("You do not have permission to delete this mapping.")
        return super().delete(request, *args, **kwargs)

