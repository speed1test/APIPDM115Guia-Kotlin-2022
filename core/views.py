from core.models import Alumno, Materia, Nota
from core.serializers import AlumnoSerializer, MateriaSerializer, NotaSerializer
from rest_framework import viewsets, permissions

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permissions = [permissions.AllowAny]
 

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer
    permissions = [permissions.AllowAny]
 

class NotaViewSet(viewsets.ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer 
    permissions = [permissions.AllowAny]