from django.db import models

# Create your models here.


class Pasajero(models.Model):
    nombre = models.CharField(max_length=200)


class Trayecto(models.Model):
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=200)


class Chofer(models.Model):
    nombre = models.CharField(max_length=200)


class Boleto(models.Model):
    fecha = models.DateTimeField('date published')
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE)
    trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE)


class Bus(models.Model):
    tipo = models.CharField(max_length=200)
    patente = models.CharField(max_length=200)
    capacidad = models.IntegerField(default=10)
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)

class Incluye(models.Model):
    asiento = models.IntegerField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    boleto = models.ForeignKey(Boleto, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):# redefinicion del metodo save() que contiene nuestro trigger
                 # Aqui ponemos el codigo del trigger -------
            bus_asiento = Bus.objects.get(bus=self.bus)
            bus_asiento.capacidad -= 1
            bus_asiento.save()
            # fin de trigger ------
            # llamada al save() original con sus parámetros correspondientes
            return super(Incluye, self).save(*args, **kwargs)


class Tramo(models.Model):
    inicio = models.CharField(max_length=200)
    fin = models.CharField(max_length=200)
    hora = models.DateTimeField('date published')
    trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
