from django.conf.urls import url
from django.urls import path, include

from .views import (
    PasajeroList,
    PasajeroView,    
    PasajeroUpdate,
    PasajeroCreate,
    PasajeroDelete
)
from . import views

urlpatterns = [

    path('', views.PasajeroList.as_view(), name='Pasajero_list'),
    path('view/<int:pk>', views.PasajeroView.as_view(), name='Pasajero_view'),
    path('new', views.PasajeroCreate.as_view(), name='Pasajero_new'),
    path('view/<int:pk>', views.PasajeroView.as_view(), name='Pasajero_view'),
    path('edit/<int:pk>', views.PasajeroUpdate.as_view(), name='Pasajero_edit'),
    path('delete/<int:pk>', views.PasajeroDelete.as_view(), name='Pasajero_delete'),
]