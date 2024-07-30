from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola mundo!")

def sucursales(request):
    texto = "conoce nuestras sucursales"
    return HttpResponse (texto)

def probando_template(request):
    mi_html = open('./django_heladeria/plantillas/index2.html')

    plantilla = Template(mi_html.read())

    mi_html.close()

    mi_contexto = Context()

    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)