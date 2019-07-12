# Se resuelve el siguiente ejercicio mediante framwork Django.

## Problema
Una agencia de buses necesita una plataforma para gestionar sus viajes. El sistema debe permitir que se ingresen diversos trayectos. Cada trayecto tendrá varios buses asignados a distintos horarios. Cada bus tendrá un solo chofer y varios pasajeros asignados a sus asientos. Todos los buses tienen la misma capacidad de 10 pasajeros sentados. Los asientos son enumerados y se reservan para cada pasajero. El sistema debe soportar el ingreso de pasajeros a un trayecto y horario en particular, ademas de permitir la asignación de choferes a sus respectivos buses.

## Modelo de datos
Escriba a continuación las tablas que utilizaría para resolver este problema con los campos y llaves de éstas. Intente hacer el sistema lo más robusto posible, pero sin incluir datos adicionales a los que se plantean acá.

## Backend
Si usted estuviera resolviendo el problema de la agencia de buses implementando una aplicación web que incluya las siguientes funcionalidades:

CRUD pasajeros, choferes, trayectos, buses.
Listar a los trayectos junto a su promedio de pasajeros.
Filtrar a todos los buses de un trayecto con más del 0% de su capacidad vendida.
Para la implementación hay que utilizar el Django y su ORM.

Nota: La aplicación debe incluir un archivo README.md explicando como instalar las dependencias del proyecto. asi como todos los supuestos considerados, se recomienda el uso de APIs en el desarrollo del test.

Frontend
Construya una función o clase en JS que recibiendo el siguiente JSON por parámetro, permita renderear una agenda semanal en html y con bloques de 30 minutos como la siguiente:

{
    "monday": [
        {"name": "Augusto", "start_time": "08:00", "end_time": "09:00"},
        {"name": "Augusto", "start_time": "09:30", "end_time": "11:00"},
        {"name": "Augusto", "start_time": "15:00", "end_time": "16:00"},
        {"name": "Augusto", "start_time": "17:00", "end_time": "19:30"}
    ],
    "tuesday": [
        {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},
        {"name": "Jorge", "start_time": "11:30", "end_time": "12:00"},
        {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},
        {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}
    ],
    "wednesday": [
        {"name": "Sebastian", "start_time": "08:00", "end_time": "09:00"},
        {"name": "Sebastian", "start_time": "10:30", "end_time": "12:00"},
        {"name": "Sebastian", "start_time": "15:00", "end_time": "16:00"},
        {"name": "Sebastian", "start_time": "17:00", "end_time": "19:30"}
    ],
    "thursday": [
        {"name": "Abdel", "start_time": "08:00", "end_time": "09:00"},
        {"name": "Abdel", "start_time": "09:30", "end_time": "12:00"},
        {"name": "Abdel", "start_time": "15:00", "end_time": "16:00"},
        {"name": "Abdel", "start_time": "17:00", "end_time": "19:30"}
    ],
    "friday": [
        {"name": "Aaron", "start_time": "08:00", "end_time": "09:00"},
        {"name": "Aaron", "start_time": "09:30", "end_time": "12:00"},
        {"name": "Aaron", "start_time": "15:00", "end_time": "16:00"},
        {"name": "Aaron", "start_time": "17:00", "end_time": "19:30"}
    ]
}

La agenda debe contener los distintos bloques y pintar con el nombre del chofer, las horas que están asignadas a un trayecto.

## Nota:

    La agenda NO debe tener interacción solo dibujarse en la pantalla
    No utilizar tablas, sólo DIVS
    La agenda debe tener un ancho de 960px y esta centrada en la pantalla

# Solución

## Explicación del modelo:

Un pasajero puede ser registrado en el sistema, por lo que no se modeló directamente con trayecto o bus. Esto permite la posibilidad de participar en un trayecto y en el mismo bus en diferentes fechas. Para lograr esto se modeló una entidad boleto, la cual contendrá la información del pasajero al que pertenece y al trayecto correspondiente. Se necesita además tener la información correspondiente del asiento que corresponde a cada pasajero y a que bus en específico. Para esto se crea una relación entre boleto y bus, ya que un bus puede tener varios boletos asociados y ese mismo boleto puede tener más de un bus correspondiente (Esto ya que el trayecto puede tener distintos tramos).

Un bus puede tener varios trayectos y un trayecto puede tener varios tramos. Si se relacionan directamente estas dos entidades, un bus no podría participar en el mismo trayecto en una fecha diferente (clave compuesta: bus, trayecto). Por lo que se crea una nueva entidad "Tramo", que corresponde al viaje correspondiente que hace cada bus en un trayecto determinado. Un bus puede hacer varios tramos diferentes y un trayecto puede tener de uno o más tramos asociados, el cual tiene su origen y final asociados. 

Psdt: No se modeló más de lo que se pidió, por lo que en un problema real se debería completar con más atributos las entidades. 

## Explicación consultas:

Listar a todos los trayectos con su promedio de pasajeros: A partir del modelo implementado (y el entendimiento del problema dado), un trayecto tiene una cantidad de pasajeros (boletos)correspondientes. Esto es lo que devuelve la consulta. 

Filtrar a todos los buses de un trayecto con más del 0% de su capacidad vendida: Cada vez que se asigna un bus un boleto con un asiento determinado, la capacidad del bus disminuye en 1. Esta consulta devuelve todos los buses los cuales su capacidad no es 10 (por defecto). En la lista de buses, si el bus tiene su capacidad completa entonces se indicará en la última columna de esa página como "capacidad completa" y sino, se indicará como "utilizado.



