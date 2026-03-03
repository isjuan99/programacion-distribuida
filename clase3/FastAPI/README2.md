## Preguntas sobre concurrencia en FastAPI

### ¿Es seguro usar variable global?
No es seguro. Cuando varios usuarios usan la API al mismo tiempo, las variables globales pueden causar problemas. Por ejemplo, si dos personas incrementan un contador global simultáneamente, ambas podrían leer el mismo valor y el contador final quedaría mal. Pasa lo mismo con las listas: si dos usuarios agregan datos a la vez, la información puede corromperse.

### ¿Dónde aparece el recurso compartido?
En este código, los recursos compartidos son:
- La lista `clientes` (todos los endpoints la modifican)
- El `contador_clientes` (varias peticiones lo incrementan)

Estos datos viven en la memoria del servidor y cualquier petición puede acceder a ellos.

### ¿Se debería usar lock en producción?
No es recomendable. Aunque los locks evitan la corrupción de datos, hacen que las peticiones esperen en fila y vuelven lenta la aplicación. En producción se usan bases de datos como PostgreSQL, MySQL o MongoDB, que están diseñadas para manejar muchas peticiones simultáneas sin problemas.

**Conclusión:** Las variables globales solo sirven para prácticas o proyectos personales. En aplicaciones reales siempre se debe usar una base de datos.
