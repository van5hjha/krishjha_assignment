from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import DoctorSerializer
from .models import Doctors

class DoctorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = DoctorSerializer
    def get_queryset(self):
        return Doctors.objects.all()
    