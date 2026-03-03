FastAPI
## Preguntas sobre concurrencia

### ¿Es seguro usar variable global?
No es seguro. Cuando varios usuarios usan la API al mismo tiempo, las variables globales pueden causar problemas como condiciones de carrera donde los datos se corrompen.

### ¿Dónde aparece el recurso compartido?
Los recursos compartidos son la lista 'clientes' y el 'contador_clientes' que están en memoria y son accedidos por todas las peticiones.

### ¿Se debería usar lock en producción?
No es recomendable porque crea cuellos de botella. En producción se usan bases de datos como PostgreSQL o MySQL.
