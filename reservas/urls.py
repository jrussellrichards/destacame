from django.conf.urls import url
from django.urls import path, include

from .views import (
    PasajeroList,
    PasajeroView,    
    PasajeroUpdate,
    PasajeroCreate,
    PasajeroDelete,
    BusList,
    BusView,    
    BusUpdate,
    BusCreate,
    BusDelete,
    ChoferList,
    ChoferView,    
    ChoferUpdate,
    ChoferCreate,
    ChoferDelete,
    TrayectoList,
    TrayectoView,    
    TrayectoUpdate,
    TrayectoCreate,
    TrayectoDelete,
    

)
from . import views

urlpatterns = [

    path('', views.Master, name='Master'),
    path('pasajero', views.PasajeroList.as_view(), name='Pasajero_list'),
    path('view/<int:pk>', views.PasajeroView.as_view(), name='Pasajero_view'),  
    url(r'pasajero/add/', PasajeroCreate.as_view(), name='Pasajero_add'),
    path('edit/<int:pk>', views.PasajeroUpdate.as_view(), name='Pasajero_edit'),
    path('delete/<int:pk>', views.PasajeroDelete.as_view(), name='Pasajero_delete'),

    path('bus/view/<int:pk>', views.BusView.as_view(), name='Bus_view'),
    url(r'bus/add/', BusCreate.as_view(), name='Bus_add'),
    path('bus/edit/<int:pk>', views.BusUpdate.as_view(), name='Bus_edit'),
    path('bus/delete/<int:pk>', views.BusDelete.as_view(), name='Bus_delete'),
    path('buses', views.BusList.as_view(), name='Bus_list'),

    path('chofer/view/<int:pk>', views.ChoferView.as_view(), name='Chofer_view'),
    path('chofer/edit/<int:pk>', views.ChoferUpdate.as_view(), name='Chofer_edit'),
    path('chofer/delete/<int:pk>', views.ChoferDelete.as_view(), name='Chofer_delete'),
    url(r'chofer/add/', ChoferCreate.as_view(), name='Chofer_add'),
    path('choferes', views.ChoferList.as_view(), name='Chofer_list'),

    path('trayecto/view/<int:pk>', views.TrayectoView.as_view(), name='Trayecto_view'),
    path('trayecto/edit/<int:pk>', views.TrayectoUpdate.as_view(), name='Trayecto_edit'),
    path('trayecto/delete/<int:pk>', views.TrayectoDelete.as_view(), name='Trayecto_delete'),
    url(r'trayecto/add/', TrayectoCreate.as_view(), name='Trayecto_add'),
    path('trayectos', views.Trayectos2, name='Trayecto_list'),
    # path('trayectos', views.TrayectoList.as_view(), name='Trayecto_list'),

    path('boleto', views.BoletorCreate.as_view(), name='create_boleto'),
    path('agenda', views.Agenda, name='agenda'),
    url(r'incluye/add/', views.IncluyeCreate.as_view(), name='incluye_add'),

]