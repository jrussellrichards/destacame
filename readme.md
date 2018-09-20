Explicación modelo: 

Un pasajero puede ser registrado en el sistema, por lo que no se modeló directamente con trayecto o bus. Esto permite la posibilidad de participar en un trayecto y en el mismo bus en diferentes fechas. Para lograr esto se modeló una entidad boleto, la cual contendrá la información del pasajero al que pertenece y al trayecto correspondiente. Se necesita además tener la información correspondiente del asiento que corresponde a cada pasajero y a que bus en específico. Para esto se crea una relación entre boleto y bus, ya que un bus puede tener varios boletos asociados y ese mismo boleto puede tener más de un bus correspondiente (Esto ya que el trayecto puede tener distintos tramos).

Un bus puede tener varios trayectos y un trayecto puede tener varios tramos. Si se relacionan directamente estas dos entidades, un bus no podría participar en el mismo trayecto en una fecha diferente (clave compuesta: bus, trayecto). Por lo que se crea una nueva entidad "Tramo", que corresponde al viaje correspondiente que hace cada bus en un trayecto determinado. Un bus puede hacer varios tramos diferentes y un trayecto puede tener de uno o más tramos asociados, el cual tiene su origen y final asociados. 

Psdt: No se modeló más de lo que se pidió, por lo que en un problema real se debería completar con más atributos las entidades. 

Explicación consultas:

Listar a todos los trayectos con su promedio de pasajeros: A partir del modelo implementado (y el entendimiento del problema dado), un trayecto tiene una cantidad de pasajeros (boletos)correspondientes. Esto es lo que devuelve la consulta. 

Filtrar a todos los buses de un trayecto con más del 0% de su capacidad vendida: Cada vez que se asigna un a un bus un boleto con un asiento determinado, la capacidad del bus disminuye en 1. Esta consulta devuelve todos los buses los cuales su capacidad no es 10 (por defecto). En la lista de buses, si el bus tiene su capacidad completa entonces se indicará en la última columna de esa página como "capacidad completa" y sino, se indicará como "utilizado.


Vista:

No entendí muy bien lo de los bloques. No se si había que añadir otros bloques adicionales al formato con el que viene la agenda. 
