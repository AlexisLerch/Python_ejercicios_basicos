class Tarea:
    def __init__(self, nombre, descripcion): # Constructor
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = 'Pendiente'

    def marcar_completada(self): # Metodo
        self.estado = 'completada'
        
    def __str__(self):
        return f'{self.nombre}: {self.descripcion} - {self.estado}'

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, nombre, descripcion):
        tarea = Tarea(nombre, descripcion)
        self.tareas.append(tarea)
        print(f'Tarea {nombre} añadida.')

    def listar_tareas(self):
        if not self.tareas:
            print('No hay tareas')
        else:
            for idx, tarea in enumerate(self.tareas, 1):
                print(f'{idx}. {tarea}')

    def marcar_tarea_completada(self, indice):
        if 1 <= indice <= len(self.tareas):
            self.tareas[indice - 1].marcar_completada()
            print('Tarea marcada como completada.')
        else:
            print('Indice de tarea no valido.')
            
    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):
            del self.tareas[indice - 1]
            print('Tarea eliminada.')
        else:
            print('Indice de tarea no valido.')
    
gestor = GestorTareas()
gestor.agregar_tarea("Comprar leche", "Ir al supermercado")
gestor.agregar_tarea("Hacer tarea de matemáticas", "Resolver problemas de álgebra")
gestor.listar_tareas()
gestor.marcar_tarea_completada(1)
gestor.listar_tareas()
gestor.eliminar_tarea(2)
gestor.listar_tareas()
