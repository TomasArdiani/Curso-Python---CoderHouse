class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.carrito = []

    def __str__(self):
        return f"Cliente({self.nombre}, {self.email}, {self.direccion}, {self.telefono})"

    def agregar_producto(self, producto):
        self.carrito.append(producto)
        print(f"Producto {producto} agregado al carrito de {self.nombre}.")

    def mostrar_carrito(self):
        if self.carrito:
            print(f"Carrito de {self.nombre}: {', '.join(self.carrito)}")
        else:
            print(f"El carrito de {self.nombre} está vacío.")
