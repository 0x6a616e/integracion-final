# Carpeta de análisis

Usamos el archivo analytics.py en un clúster de Google Cloud con el comando

~~~bash
spark-submit --master yarn analytics.py
~~~

y se generaron los archivos que están en esa carpeta, está automatizado porque
hace una solicitud a la API de datos para obtener la información más reciente
y la procesa.
