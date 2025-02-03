class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.estado = 'Disponible'

    def prestar(self):
        if self.estado == 'Disponible':
            self.estado = 'Prestado'
            return True
        return False

    def devolver(self):
        if self.estado == 'Prestado':
            self.estado = 'Disponible'
            return True
        return False

    def __str__(self):
        return f'{self.titulo} por {self.autor} (ISBN: {self.isbn}) - Estado: {self.estado}'

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, titulo, autor, isbn):
        libro = Libro(titulo,autor, isbn)
        self.libros.append(libro)

    def listar_libros(self):
        for libro in self.libros:
            print(libro)
        """if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            for idx, libro in enumerate(self.libros, 1):
                print(f'{idx}. {libro}')"""

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros:
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "isbn" and valor == libro.isbn:
                resultados.append(libro)
        return resultados

    def prestar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                if libro.prestar():
                    print(f"Libro '{libro.titulo}' ha sido prestado.")
                    return True
                else:
                    print("El libro ya está prestado.")
                    return False
        print("Libro no encontrado.")
        return False

    def devolver_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                if libro.devolver():
                    print(f"Libro '{libro.titulo}' ha sido devuelto.")
                    return True
                else:
                    print("El libro ya estaba disponible.")
                    return False
        print("Libro no encontrado.")
        return False

def menu():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro("1984", "George Orwell", "9780451524935")
    biblioteca.agregar_libro("To Kill a Mockingbird", "Harper Lee", "9780446310789")
    while True:
        print('______________________________')
        print('MENU PRINCIPAL')
        print('1: Agregar libro')
        print('2: Listar libros')
        print('3: Buscar libro')
        print('4: Prestar libro')
        print('5: devolver libro')
        print('0: Para salir')
        print('______________________________')

        opcion = input("Por favor ingrese una opcion: ")

        if opcion == '1':
            titulo = input('Ingrese el titulo del libro: ')
            autor = input('Ingrese el autor del libro: ')
            isbn = input('Ingrese el isbn del libro: ')
            biblioteca.agregar_libro(titulo, autor, isbn)
            
        elif opcion == "2":
            biblioteca.listar_libros()

        elif opcion == '3':
            criterio = input("Buscar por (titulo/autor/isbn): ").lower()
            if criterio in ["titulo", "autor", "isbn"]:
                valor = input("Valor: ")
                resultados = biblioteca.buscar_libro(criterio, valor)
                for libro in resultados:
                    print(libro)
            else:
                print("Criterio de búsqueda no válido.")

        elif opcion == '4':
            isbn = input('Ingresa elISBN del libro a prestar: ')
            biblioteca.prestar_libro(isbn)
            
        elif opcion == '5':
            isbn = input('Ingresa elISBN del libro a devolver: ')
            biblioteca.devolver_libro(isbn)
            


if __name__ == '__main__':
    menu()
