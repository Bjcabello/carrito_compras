class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        # Verificar si el carrito ya existe en la sesión
        if 'carrito' not in self.session:
            self.session['carrito'] = {}
        self.carrito = self.session['carrito']

    def add(self, producto):
        id = str(producto.id)
        if id not in self.carrito:
            # Si el producto no está en el carrito, agregarlo
            self.carrito[id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'precio': producto.precio,
                'cantidad': 1,
                'acumulado': producto.precio,  # Agregado el campo 'acumulado'
            }
        else:
            # Si el producto ya está en el carrito, incrementar la cantidad y el precio acumulado
            self.carrito[id]['cantidad'] += 1
            self.carrito[id]['acumulado'] += producto.precio
        self.save()

    def delete(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            # Eliminar el producto del carrito si está presente
            del self.carrito[id]
            self.save()

    def subtract(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            # Restar uno a la cantidad y al precio acumulado si la cantidad es mayor que cero
            self.carrito[id]['cantidad'] -= 1
            self.carrito[id]['acumulado'] -= producto.precio
            # Eliminar el producto si la cantidad llega a cero
            if self.carrito[id]['cantidad'] <= 0:
                self.delete(producto)
            self.save()

    def clear(self):
        # Limpiar el carrito
        self.session['carrito'] = {}
        self.session.modified = True

    def save(self):
        # Guardar el carrito en la sesión
        self.session['carrito'] = self.carrito
        self.session.modified = True

    
