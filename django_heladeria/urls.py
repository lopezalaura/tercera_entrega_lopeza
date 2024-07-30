from django.contrib import admin
from django.urls import path 
from views import saludo, sucursales , probando_template

urlpatterns = [
    path('adming', admin.site.urls),
    path('saludo/', saludo),
    path('sucursales/', sucursales),
    path('probando_template/', probando_template),
]