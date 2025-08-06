from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import DoctorSerializer
from .models import Doctors
from rest_framework.exceptions import PermissionDenied

class DoctorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctors.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
          serializer.save(creator=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.creator != self.request.user:
            raise PermissionDenied("You do not have permission to access this doctor.")
        return obj