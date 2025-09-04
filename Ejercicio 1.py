class Nodo:
    def __init__(self, curso):
        self.curso = curso
        self.sig = None

class ListaCursos:
    def __init__(self):
        self.cabecera = None

    def agregar(self, curso):
        nuevo = Nodo(curso)
        if self.cabecera is None:
            self.cabecera = nuevo
        else:
            nodo = self.cabecera
            while nodo.sig:
                nodo = nodo.sig
            nodo.sig = nuevo

    def mostrar(self):
        nodo = self.cabecera
        while nodo:
            print(f"{nodo.curso['hora_inicio']} - {nodo.curso['codigo']} - {nodo.curso['nombre']}")
            nodo = nodo.sig

    def ordenar(self):
        self.cabecera = self.merge_sort(self.cabecera)

    def merge_sort(self, cabeza):
        if cabeza is None or cabeza.sig is None:
            return cabeza
        
        medio = self.conseguir_medio(cabeza)
        medio_sig = medio.sig
        medio.sig = None

        izquierda = self.merge_sort(cabeza)
        derecha = self.merge_sort(medio_sig)

        return self.merge(izquierda, derecha)

    def conseguir_medio(self, cabeza):
        if cabeza is None:
            return cabeza
        lento = cabeza
        rapido = cabeza
        while rapido.sig and rapido.sig.sig:
            lento = lento.sig
            rapido = rapido.sig.sig
        return lento

    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.curso["hora_inicio"] <= b.curso["hora_inicio"]:
            resultado = a
            resultado.sig = self.merge(a.sig, b)
        else:
            resultado = b
            resultado.sig = self.merge(a, b.sig)
        return resultado

    def buscar(self, hora):
        nodo = self.cabecera
        while nodo:
            if nodo.curso["hora_inicio"] == hora:
                return nodo
            nodo = nodo.sig
        return None

#--------------------------------------------------

cursos = [
    {"codigo": "MAT101", "nombre": "Matemáticas I", "hora_inicio": "08:00"},
    {"codigo": "FIS202", "nombre": "Física II", "hora_inicio": "10:30"},
    {"codigo": "PROG305", "nombre": "Programación Avanzada", "hora_inicio": "09:15"},
    {"codigo": "HIST110", "nombre": "Historia Universal", "hora_inicio": "07:45"},
    {"codigo": "QUIM150", "nombre": "Química General", "hora_inicio": "14:00"}
]

lista = ListaCursos()


def implementar():
    for curso in cursos:
        lista.agregar(curso)

def demostrar():
    print("\nLa lista de cursos es la siguiente:")
    lista.mostrar()

def ordenamiento():
    print("\nOrdenando la lista por hora de inicio...")
    lista.ordenar()
    lista.mostrar()
    
def busqueda():
    print("\nSe ha iniciado un proceso de búsqueda...")
    hora = input("Ingrese la hora que desea buscar: ")
    proceso = lista.buscar(hora)
    if proceso is None:
        print("No se ha encontrado curso en esa respectiva hora.")
    else:
        print(f"Curso encontrado a las {hora}: {proceso.curso['nombre']}")


implementar()
demostrar()
ordenamiento()
busqueda()