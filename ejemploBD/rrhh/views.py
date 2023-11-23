from django.shortcuts import render
from rrhh.models import Empleado
from django.db.models import Avg,Max,Min,Sum,Count

# Create your views here.
def index(request):
    return render(request, 'consultas.html')

def ejecutar(request,id):
    empleados = Empleado.objects.all()
    cantidad = Empleado.objects.all().count()
    
    data = {'empleados': empleados, 'cantidad':cantidad}
    return render(request, 'listadoEmpleados.html', data)

def ejecutar_salario(request):
    empleados = Empleado.objects.all()
    promedio=Empleado.objects.all().aggregate(Avg('salario'))
    maxSalario=Empleado.objects.all().aggregate(Max('salario'))
    minSalario=Empleado.objects.all().aggregate(Min('salario'))
    sumaTotalSalario=Empleado.objects.all().aggregate(Sum('salario'))
    cantidadEmpleados=Empleado.objects.all().aggregate(Count('idEmpleado'))

    data = {'empleados': empleados,'promedio':promedio,'maxSalario': maxSalario,
            'minSalario':minSalario,'sumaTotalSalario':sumaTotalSalario,
            'cantidadEmpleados':cantidadEmpleados,
            }
    return render(request,'listaSalarioEmpleados.html',data )

def ejecutar_fitros(request):
    empleados = Empleado.objects.all()
    deptoId50=Empleado.objects.filter(departamentoId=50).count()
    empleados50Sh=Empleado.objects.filter(departamentoId=50,cargoId='SH_CLERK')
    empleados50ShTotal=Empleado.objects.filter(departamentoId=50,cargoId='SH_CLERK').count()
    data={'empleados': empleados,
          'deptoId50': deptoId50,'empleados50Sh':empleados50Sh ,
          'empleados50ShTotal':empleados50ShTotal ,
          }

    return render(request,'listaEmpleadosFiltro.html',data)

def lista_stevens(request):
    empleadoStevens=Empleado.objects.filter(nombre='Steven')
    data={'empleadoStevens': empleadoStevens}

    return render(request,'listaStevens.html',data)

def lista_di(request):
    empleadoDi=Empleado.objects.filter(nombre__startswith='Di')
    data={'empleadoDi': empleadoDi,}

    return render(request,'listaDi.html',data)

def lista_lli(request):
    empleadolli=Empleado.objects.filter(nombre__contains='lli')
    data={'empleadolli':empleadolli,}

    return render(request,'listalli.html',data)
    
    

            