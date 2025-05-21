# mappings/urls.py
from django.urls import path
from .views import MappingListCreateView, PatientMappingsAndDeleteView

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('<int:id>/', PatientMappingsAndDeleteView.as_view(), name='patient-mappings'),
]
