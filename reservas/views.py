from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

from reservas.models import Pasajero, Bus, Trayecto, Chofer, Boleto, Incluye
from django.shortcuts import render

class PasajeroList(ListView):
    model = Pasajero

class PasajeroView(DetailView):
    model = Pasajero

class PasajeroCreate(CreateView):
    model = Pasajero
    fields = ['nombre']
    success_url = reverse_lazy('Pasajero_list')

class PasajeroUpdate(UpdateView):
    model = Pasajero
    fields = ['nombre']
    success_url = reverse_lazy('Pasajero_list')

class PasajeroDelete(DeleteView):
    model = Pasajero
    success_url = reverse_lazy('Pasajero_list')

class BusList(ListView):
    model = Bus
    capacidades=Bus.objects.all()


class BusView(DetailView):
    model = Bus

class BusCreate(CreateView):
    model = Bus
    fields = ['tipo','patente','chofer']
    success_url = reverse_lazy('Bus_list')

class BusUpdate(UpdateView):
    model = Bus
    fields = ['tipo','patente','capacidad','chofer']
    success_url = reverse_lazy('Bus_list')

class BusDelete(DeleteView):
    model = Bus
    success_url = reverse_lazy('Bus_list')

class ChoferList(ListView):
    model = Chofer

class ChoferView(DetailView):
    model = Chofer

class ChoferCreate(CreateView):
    model = Chofer
    fields = ['nombre']
    success_url = reverse_lazy('Chofer_list')

class ChoferUpdate(UpdateView):
    model = Chofer
    fields = ['nombre']
    success_url = reverse_lazy('Chofer_list')

class ChoferDelete(DeleteView):
    model = Chofer
    success_url = reverse_lazy('Chofer_list')

class TrayectoList(ListView):
    model = Trayecto

class TrayectoView(DetailView):
    model = Trayecto

class TrayectoCreate(CreateView):
    model = Trayecto
    fields = ['valor','descripcion']
    success_url = reverse_lazy('Trayecto_list')

class TrayectoUpdate(UpdateView):
    model = Trayecto
    fields = ['valor','descripcion']
    success_url = reverse_lazy('Trayecto_list')

class TrayectoDelete(DeleteView):
    model = Trayecto
    success_url = reverse_lazy('Trayecto_list')

class BoletorCreate(CreateView):
    model = Boleto
    fields = ['pasajero','fecha','trayecto']
    success_url = reverse_lazy('Master')

def asignacion_bus_trigger(request, bus, boleto):
    bus_asignado = Bus.objects.get(id=bus)			
    boleto_comprado = Boleto.objects.get(id=boleto)			
    incluye = Incluye.objects.create(bus=bus_asignado, boleto=boleto_comprado)	
    incluye.save()							
    return HttpResponse("ok")

class IncluyeCreate(CreateView):
    model = Incluye
    fields = ['boleto','bus','asiento']
    success_url = reverse_lazy('Trayecto_list')
 
def Master (request):
    return render(request, 'reservas/master.html', {})

def Agenda(request):
    return render(request, 'reservas/agenda.html', {})