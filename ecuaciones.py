# -*- coding:utf-8 -*-
from pila import Pila
from nodo import Nodo
import re
import sys
from sys import stdin


class ArbolPosFijo:
    diccionario={}
    diccionarioSintactico={'Expresiones':[],'Terminales':[]}

    def evaluar(self, arbol):
        if arbol.valor=='+':
            return self.evaluar(arbol.izq)+self.evaluar(arbol.der)
        if arbol.valor=='-':
            return self.evaluar(arbol.izq)-self.evaluar(arbol.der)
        if arbol.valor=='*':
           return self.evaluar(arbol.izq)*self.evaluar(arbol.der)
        if arbol.valor=='/':
           return self.evaluar(arbol.izq)/self.evaluar(arbol.der)
        try:
           return int(arbol.valor)
        except:
          return (self.getValorDiccionario(arbol.valor))

    def retornarHijos(self,text,arbol):
        if arbol!=None:
            return text+""+self.retornarHijos(text,arbol.izq)+""+self.retornarHijos(text,arbol.der)+""+arbol.valor
        else:
            return ""
        

    def evaluarSintaxis(self,arbol):
        if re.match('[-|=|+|*|/]',arbol.valor):
            text=""
            text+="|"+arbol.valor+"|"+self.retornarHijos("",arbol)
            self.diccionarioSintactico['Expresiones'].append(text[:len(text) - 1])
            self.diccionarioSintactico['Terminales'].append("")
        else:
            self.diccionarioSintactico['Expresiones'].append("")
            self.diccionarioSintactico['Terminales'].append(arbol.valor)

    def addDiccionario(self,indice,valor):
        self.diccionario[indice]=valor

    def getValorDiccionario(self,indice):
        return self.diccionario.get(indice)

    def printDiccionario(self):
         for i in self.diccionario:
             print ("{} = {}".format(i,self.getValorDiccionario(i)))

    def construirArbol(self, posfijo):
        posfijo.pop()
        variable=posfijo.pop()
        pilaOperador = Pila()
        for caracter in posfijo :
            if (caracter == '+' or caracter == '-' or caracter == '*' or caracter == '/'):
                arbol = Nodo(caracter)
                arbol.der = pilaOperador.desapilar()
                arbol.izq = pilaOperador.desapilar()
                pilaOperador.apilar(arbol)
            else:
                arbol = Nodo(caracter)
                pilaOperador.apilar(arbol)
            self.evaluarSintaxis(arbol)
        arbol = pilaOperador.desapilar()
        self.addDiccionario(variable,self.evaluar(arbol))
        arbol1 = Nodo("=")
        arbol1.izq = arbol
        arbol1.der = Nodo(variable)
        self.evaluarSintaxis(arbol1.der)
        self.evaluarSintaxis(arbol1)
        return self.evaluar(arbol)

    def imprimirSintaxis(self):
        tam=len(self.diccionarioSintactico['Terminales'])
        for i in range(1,tam+1):
            print("Terminales: ",self.diccionarioSintactico['Terminales'][tam-i])
            print("Expresiones: ",self.diccionarioSintactico['Expresiones'][tam-i])
            print("=============================================================")
        
    
    def imprimirTabla(self,a1 , a2):
        a = 0
        for m in a1:
            print(a1[a] + "   " + a2[a])
            a = a+1
        print("====================================")


    def evaluarCaracteres(self, aux, l1 , l2):
        errores = 0
        for x in aux:
            if re.match('^[-+]?[0-9]+$', x):
                l1.append("Num")
                l2.append(x)
            elif re.match('[-|=|+|*|/]', x):
                l1.append("Oper")
                l2.append(x)
            elif re.match('^[a-zA-Z_][a-zA-Z0-9_]*$', x):
                l1.append("Var")
                l2.append(x)
            else:
                l1.append("TOKEN NO VALIDO")
                l2.append(x)
                errores+=1
        return errores


obj = ArbolPosFijo()
print("INGRESE LA ECUACION:")
while True:
    expresion = stdin.readline().split()
    if not expresion:
        print(" ==========  RESULTADO ==========  ")
        obj.printDiccionario()
        #obj.imprimirTabla(listaExpresion,listaTerminal)
        break
    print (' '.join(expresion))
    print ("El valor resultado es: "+ str(obj.construirArbol(expresion)))
    obj.imprimirSintaxis()
