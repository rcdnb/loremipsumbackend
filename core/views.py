from django.shortcuts import render
from rest_framework import viewsets
from .models import Projeto
from .serializers import ProjetoSerializer
from django_filters import rest_framework as filters



class ProjetoFilter(filters.FilterSet):
    nomeProj = filters.CharFilter(field_name="nome", lookup_expr='icontains')
    riscoProj = filters.CharFilter(field_name="risco", lookup_expr='icontains')
    valorProj = filters.NumberFilter(field_name="valor", lookup_expr='icontains')
       
    class Meta:
        model = Projeto
        fields = '__all__'

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProjetoFilter
    
