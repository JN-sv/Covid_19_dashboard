Dashboard Covid19

Se han obtenido datos del Centro Europeo para la prevencion y control de enfermedades (https://www.ecdc.europa.eu
) en lo relativo a los datos de Europa y del Instituto Carlos III para España.
Hay informaciones de covid19 por todas partes pero nada que se pudiera descargar sin pagar

El objetivo es represntar los datos de contagios, fallecidos y vacunados en sus distintas opciones por paises, toda Europa, por CCAA en España durante el año 2021 

Se han limpiado y acondicionado los datos para su fácil tratamiento y se han subido a una base de datos Mongodb Atlas en la nube.

Se hizo una API para hacer peticiones al vuelo sobre cada uno de los datos de Europa por paises con el numero de personas contagiadas, fallecidas y vacunadas y de España igualmente por CC AA en sus respectivas colecciones
También y para comprobar la correlación del desempleo con esos datos se ha cargado en la base de datos el desempleo por mes del Eurostat, agencia estadística de la Unión Europea

por último se ha hecho un dashboard en "streamlit" a fin de presentar de forma amigable y con gráficos los datos al usuario.