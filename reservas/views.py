from django.shortcuts import render
from .models import Pasajero
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class PasajeroList(ListView):
    model = Pasajero


class PasajeroDetail(DetailView):
    model = Pasajero


class PasajeroCreation(CreateView):
    model = Pasajero
    success_url = reverse('pasajeros:list')
    fields = ['nombre']

class PasajeroUpdate(UpdateView):
    model = Pasajero
    success_url = reverse('Pasajero:list')
    fields = ['name']

class PasajeroDelete(DeleteView):
    model = Pasajero
    success_url = reverse('courses:list')