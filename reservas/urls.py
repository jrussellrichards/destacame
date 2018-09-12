from django.conf.urls import url
from django.urls import path, include

from .views import (
    PasajeroList,
    PasajeroDetail,    
    PasajeroUpdate,
    PasajeroCreation,
    PasajeroDelete
)

urlpatterns = [

    url(r'^$', PasajeroList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PasajeroDetail.as_view(), name='detail'),
    url(r'^nuevo$', PasajeroCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', PasajeroUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', PasajeroDelete.as_view(), name='delete'),
]