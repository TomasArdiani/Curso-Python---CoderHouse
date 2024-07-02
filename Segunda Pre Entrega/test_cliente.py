from mi_paquete import Cliente

cliente = Cliente("Tomas Ardiani", "tomi.ardiani@gmail.com", "Vivo aca 29 9D", "261536584")

print(cliente)

cliente.agregar_producto("Monitor")
cliente.agregar_producto("Teclado")

cliente.mostrar_carrito()
