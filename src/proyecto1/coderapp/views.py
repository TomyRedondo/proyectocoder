from django.http import HttpResponse
from django.shortcuts import render
from coderapp.models import Profesor


def leer_profesor(request):
    print("Vista Profesor")
    profe = Profesor(nombre="Alicia", apellido="Japo", email="ali.japo@test.com")
    profe.save()
    return HttpResponse("El profesor se creo exitosamente")


def leer_alumnos(request):
    contexto = {
        "nombre": "Milu",
        "apellido": "Ibañez",
        "edad": 29,
        "cursos": ["Alemán", "Japonés", "Doctorado Bioq."]
    }
    return render(request, 'plantilla.html', contexto)

def index(request):
    return render(request, 'index.html')

def profesores(request):
    return HttpResponse('Vista profesor')

def estudiantes(request):
    return HttpResponse('Vista estudiante')

def cursos(request):
    return HttpResponse("Vista curso")

def entregables(request):
    return HttpResponse("Vista entregable")