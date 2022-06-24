from datetime import datetime,date
from django.http import HttpResponse
"""
from django.template import Template,Context,loader

"""
from django.shortcuts import render

def saludo(request):

    nombre="Fede"
    apellido="SM"
    fecha=datetime.now()
    temas=["Plantillas","Modelos","Formularios","Vistas"]
    """
    arch=open("C:/Users/BASSTARD/Desktop/git/djangoCodoACodo/templates/plantilla.html")
    plt=Template(arch.read())
    arch.close()
    ctx=Context({"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha,"temas_curso":temas})
    documento=plt.render(ctx)
    return HttpResponse(documento)
    """
    return render(request,"plantilla.html",{"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha,"temas_curso":temas})
def curso(request):
    fecha=datetime.now()
    return render(request,"curso.html",{"now":fecha})   

def saludo_html(request):
    documento="""<html><body><h1>Hola a todos!</h1></body></html>"""
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta Luego!")

def get_fecha(request):
    fecha_actual=datetime.now()
    documento="""<html><body><h1>Fecha:%s</h1><body></html>"""%fecha_actual
    return HttpResponse(documento)        

def calcular_edad(request,edad,año):
    
    periodo=año-date.today().year
    edad_futura=edad+periodo
    documento="""<html><body><h1>En el año %s tendras %s años</h1><body></html>"""%(año,edad_futura)
    return HttpResponse(documento)  
