# Clase Nodo: representa cada página en el historial
class Nodo:
    def __init__(self, url, titulo, hora):
        self.url = url          # Dirección de la página web
        self.titulo = titulo    # Título de la página
        self.hora = hora        # Hora en que fue visitada
        self.sig = None         # Puntero al siguiente nodo
        self.ant = None         # Puntero al nodo anterior


# Clase ListaDoble: maneja el historial como lista doblemente enlazada
class ListaDoble:
    def __init__(self):
        self.inicio = None  # Primer nodo de la lista
        self.fin = None     # Último nodo de la lista
        self.actual = None  # Nodo que representa la página actual

    # Agregar una nueva página al historial
    def agregar(self, url, titulo, hora):
        nuevo = Nodo(url, titulo, hora)  # Se crea el nodo
        if self.inicio is None:          # Si la lista está vacía
            self.inicio = self.fin = self.actual = nuevo
        else:                            # Si ya hay elementos
            self.fin.sig = nuevo         # El último nodo apunta al nuevo
            nuevo.ant = self.fin         # El nuevo nodo apunta hacia atrás
            self.fin = nuevo             # El nuevo nodo se convierte en el último
            self.actual = nuevo          # Se actualiza como página actual

    # Mostrar todo el historial
    def mostrar(self):
        nodo = self.inicio
        print("\nHistorial de navegación:")
        while nodo:  # Recorre la lista desde el inicio
            # Marca la página actual
            marca = " <= (Actual)" if nodo == self.actual else ""
            print(f"[{nodo.titulo}] {nodo.url} ({nodo.hora}){marca}")
            nodo = nodo.sig
        if self.inicio is None:
            print("Historial vacío.")

    # Buscar una página por URL o título
    def buscar(self, clave):
        nodo = self.inicio
        while nodo:  # Se recorre todo el historial
            if nodo.url == clave or nodo.titulo.lower() == clave.lower():
                return nodo
            nodo = nodo.sig
        return None

    # Eliminar una página del historial
    def eliminar(self, url):
        nodo = self.buscar(url)  # Se localiza la página
        if nodo is None:
            print(f"No se encontró la página {url}.")
            return

        # Caso 1: la lista solo tiene un nodo
        if nodo == self.inicio and nodo == self.fin:
            self.inicio = self.fin = self.actual = None

        # Caso 2: eliminar el primer nodo
        elif nodo == self.inicio:
            self.inicio = nodo.sig
            self.inicio.ant = None
            if self.actual == nodo:
                self.actual = self.inicio

        # Caso 3: eliminar el último nodo
        elif nodo == self.fin:
            self.fin = nodo.ant
            self.fin.sig = None
            if self.actual == nodo:
                self.actual = self.fin

        # Caso 4: eliminar un nodo intermedio
        else:
            nodo.ant.sig = nodo.sig
            nodo.sig.ant = nodo.ant
            if self.actual == nodo:
                self.actual = nodo.ant

        print(f"La página {url} ha sido eliminada correctamente.")

    # Retroceder a la página anterior
    def retroceder(self):
        if self.actual and self.actual.ant:
            self.actual = self.actual.ant
            print(f"Retrocediste a: {self.actual.titulo} ({self.actual.url})")
        else:
            print("No hay páginas anteriores.")

    # Avanzar a la página siguiente
    def avanzar(self):
        if self.actual and self.actual.sig:
            self.actual = self.actual.sig
            print(f"Avanzaste a: {self.actual.titulo} ({self.actual.url})")
        else:
            print("No hay páginas siguientes.")


#-----------------------------------------------------------------------------
# Menú de interacción con el usuario
def menu():
    lista = ListaDoble()

    # Se agregan páginas iniciales al historial
    lista.agregar("google.com", "Google", "10:00 AM")
    lista.agregar("wikipedia.org", "Wikipedia", "10:05 AM")
    lista.agregar("github.com", "GitHub", "10:10 AM")
    lista.agregar("stackoverflow.com", "Stack Overflow", "10:15 AM")

    # Menú principal
    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar historial")
        print("2. Agregar nueva página")
        print("3. Retroceder")
        print("4. Avanzar")
        print("5. Buscar página")
        print("6. Eliminar página")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lista.mostrar()
            
        elif opcion == "2":
            url = input("Ingrese la URL: ")
            titulo = input("Ingrese el título: ")
            hora = input("Ingrese la hora (ej: 10:30 AM): ")
            lista.agregar(url, titulo, hora)
            print("Página agregada correctamente.")
            
        elif opcion == "3":
            lista.retroceder()
            
        elif opcion == "4":
            lista.avanzar()
            
        elif opcion == "5":
            clave = input("Ingrese URL o título a buscar: ")
            nodo = lista.buscar(clave)
            if nodo:
                print(f"Encontrado: {nodo.titulo} ({nodo.url}) - {nodo.hora}")
            else:
                print("No se encontró la página.")
                
        elif opcion == "6":
            url = input("Ingrese la URL a eliminar: ")
            lista.eliminar(url)
            
        elif opcion == "7":
            print("Saliendo del historial...")
            break
        
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar el programa
menu()
