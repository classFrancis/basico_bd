"""
URL configuration for ejemploBD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rrhh import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('consultar/<int:id>', views.ejecutar, name='ejecutar'),
    path('sueldos/',views.ejecutar_salario,name='salarios'),
    path('filtros/',views.ejecutar_fitros,name='fitros'),
    path('filtro_steven/',views.lista_stevens,name='lista_steven'),
    path('filtro_di/',views.lista_di,name='lista_di'),
    path('filtro_lli/',views.lista_lli,name='lista_lli'),
    

]
