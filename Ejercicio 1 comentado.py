# Clase que representa un Nodo de la lista enlazada
class Nodo:
    def __init__(self, curso):
        self.curso = curso   # Guarda la información del curso (diccionario con código, nombre y hora)
        self.sig = None      # Apunta al siguiente nodo de la lista (None significa fin de lista)

# Clase que representa la lista enlazada de cursos
class ListaCursos:
    def __init__(self):
        self.cabecera = None   # La cabecera apunta al primer nodo de la lista

    # Método para agregar un curso a la lista enlazada
    def agregar(self, curso):
        nuevo = Nodo(curso)     # Se crea un nuevo nodo con la información del curso
        if self.cabecera is None:   # Si la lista está vacía, el nuevo nodo será la cabecera
            self.cabecera = nuevo
        else:   # Si no está vacía, se recorre la lista hasta el final para insertar el nodo
            nodo = self.cabecera
            while nodo.sig:
                nodo = nodo.sig
            nodo.sig = nuevo

    # Método para mostrar todos los cursos de la lista
    def mostrar(self):
        nodo = self.cabecera
        while nodo:   # Recorre la lista desde la cabecera hasta el final
            print(f"{nodo.curso['hora_inicio']} - {nodo.curso['codigo']} - {nodo.curso['nombre']}")
            nodo = nodo.sig

    # Método que inicia el proceso de ordenamiento (merge sort)
    def ordenar(self):
        self.cabecera = self.merge_sort(self.cabecera)

    # Algoritmo Merge Sort adaptado a listas enlazadas
    def merge_sort(self, cabeza):
        # Caso base: lista vacía o de un solo nodo
        if cabeza is None or cabeza.sig is None:
            return cabeza
        
        # Se encuentra el nodo medio para dividir la lista en dos
        medio = self.conseguir_medio(cabeza)
        medio_sig = medio.sig
        medio.sig = None   # Se corta la lista en dos mitades

        # Llamadas recursivas para ordenar ambas mitades
        izquierda = self.merge_sort(cabeza)
        derecha = self.merge_sort(medio_sig)

        # Se combinan ambas mitades ya ordenadas
        return self.merge(izquierda, derecha)

    # Método para conseguir el nodo del medio usando punteros lento y rápido
    def conseguir_medio(self, cabeza):
        if cabeza is None:
            return cabeza
        lento = cabeza
        rapido = cabeza
        # El puntero rápido avanza de dos en dos, el lento de uno en uno
        while rapido.sig and rapido.sig.sig:
            lento = lento.sig
            rapido = rapido.sig.sig
        return lento

    # Método para fusionar dos listas ordenadas en una sola
    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        # Se compara la hora de inicio de los cursos para ordenarlos
        if a.curso["hora_inicio"] <= b.curso["hora_inicio"]:
            resultado = a
            resultado.sig = self.merge(a.sig, b)
        else:
            resultado = b
            resultado.sig = self.merge(a, b.sig)
        return resultado

    # Método para buscar un curso por su hora de inicio
    def buscar(self, hora):
        nodo = self.cabecera
        while nodo:   # Se recorre la lista nodo por nodo
            if nodo.curso["hora_inicio"] == hora:   # Si se encuentra la hora, retorna el nodo
                return nodo
            nodo = nodo.sig
        return None   # Si no se encuentra, retorna None


#--------------------------------------------------
# Lista de cursos de ejemplo
cursos = [
    {"codigo": "MAT101", "nombre": "Matemáticas I", "hora_inicio": "08:00"},
    {"codigo": "FIS202", "nombre": "Física II", "hora_inicio": "10:30"},
    {"codigo": "PROG305", "nombre": "Programación Avanzada", "hora_inicio": "09:15"},
    {"codigo": "HIST110", "nombre": "Historia Universal", "hora_inicio": "07:45"},
    {"codigo": "QUIM150", "nombre": "Química General", "hora_inicio": "14:00"}
]

# Se crea la lista enlazada de cursos
lista = ListaCursos()

# Función para insertar todos los cursos en la lista
def implementar():
    for curso in cursos:
        lista.agregar(curso)

# Función para mostrar los cursos de la lista
def demostrar():
    print("\nLa lista de cursos es la siguiente:")
    lista.mostrar()

# Función para ordenar y mostrar la lista
def ordenamiento():
    print("\nOrdenando la lista por hora de inicio...")
    lista.ordenar()
    lista.mostrar()
    
# Función para realizar una búsqueda por hora
def busqueda():
    print("\nSe ha iniciado un proceso de búsqueda...")
    hora = input("Ingrese la hora que desea buscar: ")
    proceso = lista.buscar(hora)
    if proceso is None:
        print("No se ha encontrado curso en esa respectiva hora.")
    else:
        print(f"Curso encontrado a las {hora}: {proceso.curso['nombre']}")

# Ejecución del programa
implementar()
demostrar()
ordenamiento()
busqueda()