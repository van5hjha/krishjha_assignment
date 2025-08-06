from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import PatientSerializer
from .models import Patients

from rest_framework.exceptions import PermissionDenied

class PatientViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patients.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.creator != self.request.user:
            raise PermissionDenied("You do not have permission to access this patient.")
        return obj