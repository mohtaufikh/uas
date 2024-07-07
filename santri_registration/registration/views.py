# registration/views.py
from rest_framework import viewsets
from .models import Santri
from .serializers import SantriSerializer

class SantriViewSet(viewsets.ModelViewSet):
    queryset = Santri.objects.all()
    serializer_class = SantriSerializer

