from tkinter import *


class NodoCoordenada:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_x1(self):
        return self.x1

    def get_y1(self):
        return self.y1

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2

    def set_x1(self, x1):
        self.x1 = x1

    def set_y1(self, y1):
        self.y1 = y1

    def set_x2(self, x2):
        self.x2 = x2

    def set_y2(self, y2):
        self.y2 = y2


class ArbolInterfaz(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Elementos del frame
        self.config(width=1000, height=350)

        self.arbol = None

        self.canvas = Canvas(self, width=1000, height=350)
        self.canvas.pack()

        self.coordenadas_raiz = NodoCoordenada(500, 0, 550, 50)

        # Nodo que se va a buscar
        self.nodo_seleccionado = None

        # Bandera para saber si ya hemos encontrado el nodo
        self.encontrado = False

        # 500 -> 490 -> (10)
        # 550 -> 530 -> (20), 50 -> 30 -> (20)

        # 1. 500 - 2.5 = 497.5
        # 1. 550 - 5 = 545, 50 - 5 = 45

        # 2. 497.5 - 2.5 = 495
        # 2. 545 - 5 = 540, 45 - 5 = 40

        self.separacion = 0

    def dibujar_arbol(self, *args):
        nodo = self.arbol.get_root_reference() if len(args) == 0 else args[0]
        coordenadas = self.coordenadas_raiz if len(args) == 0 else args[1]
        separacion = self.separacion if len(args) == 0 else args[2]

        if nodo is not None:
            self.encontrado = False

            if nodo.is_leaf() and nodo.get_data() is not None:
                # Dibujamos el nodo

                # Comprobamos si este nodo es el nodo seleccionado
                if nodo.get_data() == self.nodo_seleccionado and not self.encontrado:
                    self.crear_nodo(coordenadas, 'blue')

                else:
                    self.crear_nodo(coordenadas)

                self.crear_texto(coordenadas, str(nodo.get_data()))

            else:
                # Comprobamos que este nodo no sea uno de relleno
                # Los nodos de relleno se usan para completar el arbol, estos tienen como dato None
                if nodo.get_data() is None:
                    return

                # Obtenemos las coordenadas del nodo izquierdo
                # Creamos un nuevo nodo con las coordenadas del nodo izquierdo
                coordenadas_izquierdo = NodoCoordenada(coordenadas.get_x1() - 160 + separacion,
                                                       coordenadas.get_y1() + 50,
                                                       (coordenadas.get_x2() - 160 + separacion) - 4,
                                                       (coordenadas.get_y2() + 50) - 4)

                coordenadas_derecho = NodoCoordenada(coordenadas.get_x1() + 160 - separacion,
                                                     coordenadas.get_y1() + 50,
                                                     (coordenadas.get_x2() + 160 - separacion) - 4,
                                                     (coordenadas.get_y2() + 50) - 4)

                # Comprobamos que tenga un nodo izquierdo
                if nodo.get_left() is not None:
                    # Comprobamos que el nodo izquierdo no sea de relleno
                    if nodo.get_left().get_data() is not None:
                        # Dibujamos una linea del punto medio del ovalo del nodo actual al punto medio del ovalo del
                        # nodo izquierdo
                        self.crear_flecha(coordenadas, coordenadas_izquierdo)

                # Comprobamos que tenga un nodo derecho
                if nodo.get_right() is not None:
                    # Comprobamos que el nodo derecho no sea de relleno
                    if nodo.get_right().get_data() is not None:
                        # Dibujamos una linea del punto medio del ovalo del nodo actual al punto medio del ovalo del
                        # nodo derecho
                        self.crear_flecha(coordenadas, coordenadas_derecho)

                # Escribimos encima de las flechas el valor del nodo y nuestro nodo
                # En caso de tener hijos, dibujamos ambos nodos, los dibujamos encima de las flechas

                # Comprobamos si el nodo actual es el que buscamos
                if nodo.get_data() == self.nodo_seleccionado and not self.encontrado:
                    self.crear_nodo(coordenadas, "blue")
                    self.encontrado = True

                else:
                    self.crear_nodo(coordenadas)

                # Imprimimos el valor del nodo en el centro del nodo
                self.crear_texto(coordenadas, str(nodo.get_data()))

                # Dibujamos los nodos izquierdos
                self.dibujar_arbol(nodo.left, coordenadas_izquierdo, separacion + 60)

                # Dibujamos los nodos derechos
                self.dibujar_arbol(nodo.right, coordenadas_derecho, separacion + 60)

        # Datos necesarios
        # Profundidad del árbol
        # Nodos en un nivel determinado
        # Lista de nodos

    def actualizar(self, arbol):
        # Limpiamos el canvas
        self.canvas.delete("all")

        # Le enviamos a la clase el árbol
        self.set_arbol(arbol)

        # Le indicamos cual nodo estamos buscando
        self.nodo_seleccionado = arbol.get_seleccionado()

        self.dibujar_arbol()

    def set_arbol(self, arbol_informacion):
        self.arbol = arbol_informacion.get_arbol_referencia()

    def crear_flecha(self, coordenada_actual, coordenada_siguiente):
        self.canvas.create_line(
            coordenada_actual.get_x1() + (coordenada_actual.get_x2() - coordenada_actual.get_x1()) / 2,
            coordenada_actual.get_y1() + (coordenada_actual.get_y2() - coordenada_actual.get_y1()) / 2,
            coordenada_siguiente.get_x1() + (
                    coordenada_siguiente.get_x2() - coordenada_siguiente.get_x1()) / 2,
            coordenada_siguiente.get_y1() + (
                    coordenada_siguiente.get_y2() - coordenada_siguiente.get_y1()) / 2,
            arrow=LAST, fill="black")

    def crear_nodo(self, coordenada_actual, color="yellow"):
        self.canvas.create_oval(coordenada_actual.get_x1(), coordenada_actual.get_y1(),
                                coordenada_actual.get_x2(), coordenada_actual.get_y2(),
                                fill=color)

    def crear_texto(self, coordenada_actual, texto):
        self.canvas.create_text(coordenada_actual.get_x1() + (coordenada_actual.get_x2() -
                                                              coordenada_actual.get_x1()) / 2,

                                coordenada_actual.get_y1() + (coordenada_actual.get_y2() -
                                                              coordenada_actual.get_y1()) / 2,
                                text=texto)
