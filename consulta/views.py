from django.shortcuts import render
from .models import Consulta


# Create your views here.
def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consulta/consulta_list.html', {'consultas': consultas})