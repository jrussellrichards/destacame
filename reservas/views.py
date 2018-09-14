from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from reservas.models import Pasajero

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