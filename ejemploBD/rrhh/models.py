# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Cargo(models.Model):

    cargoId = models.CharField(primary_key = True,max_length = 10)
    cargoNombre = models.CharField(max_length = 35)
    minSalario = models.IntegerField()
    maxSalario = models.IntegerField()

    def __str__(self):
        return "{}".format(self.cargoNombre)

class Departamento(models.Model):

    departId = models.IntegerField(primary_key = True)
    departNombre = models.CharField(max_length = 30)

    def __str__(self):
        return "{}".format(self.departNombre)

   
class Empleado(models.Model):

    idEmpleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellidoPaterno = models.CharField(max_length=60)
    apellidoMaterno = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)
    
    fechaContratacion = models.DateField()
    fechaNacimiento= models.DateField()
    
    salario = models.IntegerField()
    comision = models.DecimalField(max_digits=5, decimal_places=2)

    cargoId = models.ForeignKey(Cargo, null = True, blank = False, on_delete = models.RESTRICT)
    departamentoId = models.ForeignKey(Departamento, null = True, blank = False,  on_delete = models.RESTRICT)
   # jefeId =models.ForeignKey(Empleado, null = True, blank = False, on_delete = models.RESTRICT)
    
    
    