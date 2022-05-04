/* 1. ¿Cuál es el nombre aeropuerto que ha tenido mayor movimiento durante el año? */
SELECT aeropuertos.NOMBRE_AEROPUERTO, count(vuelos.ID_AEROPUERTO) as MovimientosEnElAño
From vuelos
LEFT JOIN aeropuertos
ON vuelos.ID_AEROPUERTO = aeropuertos.ID_AEROPUERTO
Group by vuelos.ID_AEROPUERTO
ORDER by count(vuelos.ID_AEROPUERTO) DESC;

/* 2. ¿Cuál es el nombre aerolínea que ha realizado mayor número de vuelos durante el año? */
SELECT aerolineas.NOMBRE_AEROLINEA, count(vuelos.ID_AEROLINEA) as VuelosEnElAño
From vuelos
LEFT JOIN aerolineas
ON vuelos.ID_AEROLINEA = aerolineas.ID_AEROLINEA
Group by vuelos.ID_AEROLINEA
ORDER by count(vuelos.ID_AEROLINEA) DESC;

/* 3. ¿En qué día se han tenido mayor número de vuelos? */
SELECT vuelos.DIA, count(vuelos.ID_AEROLINEA) as VuelosEnElDia
From vuelos
Group by vuelos.DIA
ORDER by count(vuelos.DIA) DESC;

/* 4. ¿Cuáles son las aerolíneas que tienen mas de 2 vuelos por día? */
SELECT aerolineas.NOMBRE_AEROLINEA, count(vuelos.ID_AEROLINEA) as VuelosEnElAño
From vuelos
LEFT JOIN aerolineas
ON vuelos.ID_AEROLINEA = aerolineas.ID_AEROLINEA
Group by vuelos.ID_AEROLINEA
HAVING count(vuelos.ID_AEROLINEA) > 2;