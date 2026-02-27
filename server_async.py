import asyncio  # Importa la librería para programación asíncrona

clientes_atendidos = 0

lock = asyncio.Lock()
# Función que maneja cada cliente (coroutine)
async def handle_client(reader, writer):

    global clientes_atendidos
    # Espera datos del cliente (máximo 1024 bytes)
    data = await reader.read(1024)


    # PASO 4: Proteger la sección crítica con lock
    async with lock:  # Solo un cliente puede incrementar a la vez

    # Incrementar contador cuando llega un nuevo cliente
        clientes_atendidos += 1
        cliente_actual = clientes_atendidos

    print(f"[Cliente {cliente_actual}] Nuevo cliente conectado")
    name = data.decode()

    print(f"Cliente recibido: {name} eres el cliente N: {clientes_atendidos}")

    # primer pso: Simulacion de tiempo de 5S
    print(f"Atendiendo a {name}... (5 segundos)")
    await asyncio.sleep(5)  #usamos el metodo que dice el profe
    print(f"Atención completada con exito...")

    # Construye el mensaje de respuesta
    response = f"Hola {name}"

    # Envía la respuesta al cliente (en bytes)
    writer.write(response.encode())

    # Espera a que los datos se envíen completamente
    await writer.drain()

    # Cierra la conexión con el cliente
    writer.close()

# Función principal del servidor
async def main():
    # Crea el servidor en la IP 0.0.0.0 y puerto 5000
    # handle_client será ejecutado por cada nueva conexión
    server = await asyncio.start_server(
        handle_client, "0.0.0.0", 5000
    )

    # Mantiene el servidor activo
    async with server:
        # El servidor queda escuchando indefinidamente
        await server.serve_forever()

# Ejecuta el evento loop principal
asyncio.run(main())
