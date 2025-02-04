"""

Añadir productos: Añadir nuevos productos al inventario.
Actualizar stock: Modificar la cantidad de stock disponible de un producto.
Consultar producto: Buscar información de un producto por su nombre o código.
Listar productos: Mostrar todos los productos en el inventario.

Requisitos:
Cada producto debe tener un nombre, código único, precio y cantidad en stock.
Utiliza clases para representar productos e inventario.
No es necesario persistir los datos en disco para este ejercicio, pero piensa en cómo podrías hacerlo.

"""

class Producto:
    def __init__(self, nombre, codigo, precio, stock):
        self.nombre = nombre
        self.codigo = codigo
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo}) - Precio: ${self.precio} - Stock: {self.stock}"
    
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, codigo, precio, stock):
        producto = Producto(nombre, codigo, precio, stock)
        self.productos.append(producto)

    def listar_productos(self):
        for producto in self.productos:
            print(producto)

    def actualizar_stock(self, codigo, nuevo_stock):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.stock = nuevo_stock
                print(f'El stock de {producto.nombre} se actualizo.')
                return
        print('producto no encontrado')

    def consultar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto

    def eliminar_producto(self, nombre):
        for i, producto in enumerate(self.productos):
            if producto.nombre == nombre:
                eliminado = self.productos.pop(i)
                print(f'Producto {eliminado.nombre} eliminado del inventario.')
                return
        
def menu():
    inventario = Inventario()
    while True:
        print('______________________________')
        print('MENU PRINCIPAL')
        print('1: Agregar producto')
        print('2: Listar producto')
        print('3: Actualizar stock')
        print('4: Consultar producto')
        print('5: Eliminar producto')
        print('0: Para salir')
        print('______________________________')

        opcion = input("Por favor ingrese una opcion: ")

        if opcion == '1':
            nombre = input('Ingrese el nombre del producto: ')
            codigo = input('Ingrese el codigo del producto: ')
            precio = input('Ingrese el precio del producto: ')
            stock = input('Ingrese el stock del producto: ')
            inventario.agregar_producto(nombre, codigo, precio, stock)

        elif opcion == '2':
            inventario.listar_productos()
            
        elif opcion == '3':
            codigo = input('Ingrese el codigo del producto: ')
            nuevo_stock = input('Ingrese el nuevo stock: ')
            inventario.actualizar_stock(codigo, nuevo_stock)

        elif opcion == '4':
            nombre = input('Ingrese el nombre del producto a buscar: ')
            print(inventario.consultar_producto(nombre))

        elif opcion == '5':
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
            

if __name__ == '__main__':
    menu()
