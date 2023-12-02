Esta es la carpeta que tiene la API para solicitar, insertar o actualizar datos,
se necesita tener un archivo .env en la carpeta con las siguientes variables de
entorno:

- MYSQL_HOST
- MYSQL_DB
- MYSQL_USER
- MYSQL_PASSWORD
- APP_SECRET

Rutas:

/data/<table>

Esta ruta con el método GET regresa todas las entradas de una tabla

/data/<table>/<field_name>/<value>

Esta ruta con el método GET regresa las entradas de la tabla que tengan un valor
determinado en cierto campo

/data/<table>

Esta ruta con el método POST inserta una nueva entrada en la tabla con los
atributos que se pasen en el form, esta protegida por JWT

/data/<table>/id

Esta ruta con el método PATCH actualiza una entrada según el id recibido y los
atributos que se mandan en el forms, esta protegida por JWT

/attr/<table>

Esta ruta con el método GET regresa las columnas de la tabla solicitada

/order/<id>

Esta ruta con el método GET regresa la información de la orden completa
