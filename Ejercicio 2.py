class Nodo:
    def __init__(self, url, titulo, hora):
        self.url = url
        self.titulo = titulo
        self.hora = hora
        self.sig = None
        self.ant = None

class ListaDoble:
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.actual = None 

    def agregar(self, url, titulo, hora):
        nuevo = Nodo(url, titulo, hora)
        if self.inicio is None:
            self.inicio = self.fin = self.actual = nuevo
        else:
            self.fin.sig = nuevo
            nuevo.ant = self.fin
            self.fin = nuevo
            self.actual = nuevo 

    def mostrar(self):
        nodo = self.inicio
        print("\nHistorial de navegación:")
        while nodo:
            marca = " <= (Actual)" if nodo == self.actual else ""
            print(f"[{nodo.titulo}] {nodo.url} ({nodo.hora}){marca}")
            nodo = nodo.sig
        if self.inicio is None:
            print("Historial vacío.")

    def buscar(self, clave):
        nodo = self.inicio
        while nodo:
            if nodo.url == clave or nodo.titulo.lower() == clave.lower():
                return nodo
            nodo = nodo.sig
        return None

    def eliminar(self, url):
        nodo = self.buscar(url)
        if nodo is None:
            print(f"No se encontró la página {url}.")
            return

        if nodo == self.inicio and nodo == self.fin:
            self.inicio = self.fin = self.actual = None
        elif nodo == self.inicio:
            self.inicio = nodo.sig
            self.inicio.ant = None
            if self.actual == nodo:
                self.actual = self.inicio
        elif nodo == self.fin:
            self.fin = nodo.ant
            self.fin.sig = None
            if self.actual == nodo:
                self.actual = self.fin
        else:
            nodo.ant.sig = nodo.sig
            nodo.sig.ant = nodo.ant
            if self.actual == nodo:
                self.actual = nodo.ant
        print(f"La página {url} ha sido eliminada correctamente.")

    def retroceder(self):
        if self.actual and self.actual.ant:
            self.actual = self.actual.ant
            print(f"Retrocediste a: {self.actual.titulo} ({self.actual.url})")
        else:
            print("No hay páginas anteriores.")

    def avanzar(self):
        if self.actual and self.actual.sig:
            self.actual = self.actual.sig
            print(f"Avanzaste a: {self.actual.titulo} ({self.actual.url})")
        else:
            print("No hay páginas siguientes.")

#-----------------------------------------------------------------------------

def menu():
    lista = ListaDoble()

    lista.agregar("google.com", "Google", "10:00 AM")
    lista.agregar("wikipedia.org", "Wikipedia", "10:05 AM")
    lista.agregar("github.com", "GitHub", "10:10 AM")
    lista.agregar("stackoverflow.com", "Stack Overflow", "10:15 AM")

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

menu()