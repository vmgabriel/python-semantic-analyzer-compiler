#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Libreria basica PILA

@author: Andres Aguirre - Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Pila(object):
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """

    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]
        """Datos que la pila a almacenar"""

    def apilar(self, x):
        """
        Agrega el elemento x a la pila.

        @param x: Dato que desea apilarse
        """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
        Si la pila está vacía levanta una excepción.

        @return: Valor que estaba guardado antes que cualquier otro
        """
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """
        Devuelve True si la lista está vacía, False si no.

        @return: si está vacia o no
        @rtype: bool
        """
        return self.items == []
