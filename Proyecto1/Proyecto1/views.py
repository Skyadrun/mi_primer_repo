from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):

    nombre="Ronald"

    apellido="Valera"

    doc_externo=open("C:/Users/Astaroth/Desktop/django/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":nombre, "apellido_persona": apellido})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse("Hasta luego alumnos de Django")

def dameFecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request, agno):

    edadActual=18
    periodo=agno-2019
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año %s tendras %s años" %(agno, edadFutura)

    return HttpResponse(documento)
