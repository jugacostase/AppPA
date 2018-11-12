from django.shortcuts import render

# Create your views here.

import json
import requests

from rest_framework import viewsets
from .models import Persona, Reporte, Tarea
from .serializers import PersonaSerializer, ReporteSerializer, TareaSerializer
from rest_framework import generics


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    def get_queryset(self):

        algo = self.request.query_params.get('correo', None)
        if algo is not None:
            queryset = Persona.objects.filter(correo=algo)
            queryset["Access-Control-Allow-Origin"] = "*"
            queryset["Access-Control-Allow-Methods"] = "GET, OPTIONS"
            queryset["Access-Control-Max-Age"] = "1000"
            queryset["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            return queryset
        else:
            queryset = Persona.objects.all()
            return queryset
   

'''
class IntegrantesSemillero(viewsets.ModelViewSet):
    queryset = Reporte.objects.filter(Persona=)
'''

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
