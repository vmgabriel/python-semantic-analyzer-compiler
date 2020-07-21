#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Estructura basica del arbol,conocido como NODO

@author: Andres Aguirre - Dalia Muñoz - Gabriel Vargas
@version: 0.1
@license: GPL
@contact: vmgabriel96@gmail.com
"""

class Nodo():
    """
    Clase centrada en crear arboles
    """
    def __init__(self,valor,izq=None,der=None):
        """
        Inicializador basico del nodo, tiene ciertas peculiaridades
        recordar que el nodo construye un B{arbol binario}

        @param valor: Dato a insertar del nodo1
        @param izq: Otro nodo basico, para generar arboles
        @param der: Otro nodo basico, para generar arboles
        @type izq: Nodo()
        @type der: Nodo()
        """
        self.valor=valor
        """Valor que almacena el dato del arbol, al no ser altamente tipado
        puede guardar cualquier dato"""
        self.izq=izq
        """Seccion izquierda del arbol que en consecuencia tambien es un arbol"""
        self.der=der
        """Seccion derecha del arbol que en consecuencia tambien es un arbol"""
