# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 22:54:14 2020

@author: Rodrigo
"""


# -*- coding: utf-8 -*-

from texttable import Texttable
import qprompt
from tabulate import tabulate
import time
start_time = time.time()

def crearGrafo():
    g = Grafo()
    while 1:

        menu = qprompt.Menu()
        menu.add("1", "Agregar nodo")
        menu.add("2", "Agregar arista")
        menu.add("3", "Bellman-Ford")
        menu.add("4", "Mostrar")
        menu.add("5", "Salir")
        choice = menu.show()

        if choice == "1":
            valor = input("Ingrese el numero del nodo: ")
            if valor not in g:
                g.agregarNodo(valor)
            else:
                print('El nodo ya existe.')
        elif choice == '2':
            origen = input("Ingrese el nodo origen: ")
            destino = input("Ingrese el nodo destino: ")
            peso = input("Ingrese el peso: ")
            if origen not in g.nodos:
                print('El nodo {} no existe'.format(origen))
            elif destino not in g.nodos:
                print('El nodo {} no existe.'.format(destino))
            else:
                if not g.existe(origen, destino):
                    g.agregarArista(origen, destino, peso)
                else:
                    print('La arista ya existe.')
     
        elif choice == '3':
            valor = input("Ingrese el nodo: ")
            origen = g.getNodo(valor)
            distancia = bellman_ford(g, origen)    
            
            if distancia != 1:
                
            
                nodos = []
                for nodo in distancia:
                    nodos.append((nodo.get_key(), distancia[nodo]))
                nodos =sorted(nodos, key=lambda tup: tup[0])        
                
                tabla = Texttable()
                row = ["Nodo"]
                row2 = ["Distancia"]
                for nodo in nodos:
                    row.append(nodo[0])
                    row2.append(nodo[1])
                tabla.add_row(row)
                tabla.add_row(row2)
                print(tabla.draw())
            else:
                print("Contiene pesos negativos")
        elif choice == "4":
            print('Nodos: ')
            for x in g:
                print(x.get_key())
            print()
     
            print('Aristas: ')
            for x in g:
                for destino in x.getNodoAdyacentes():
                    w = x.peso(destino)
                    print('(Origen=: {}, Destino: {}, peso: {}) '.format(x.get_key(),
                                                                 destino.get_key(), w))
            print()
     
        elif choice == '5':
            break


class Grafo:
    def __init__(self):
        self.nodos = {}
 
    def agregarNodo(self, numero):
        nodo = Nodo(numero)
        self.nodos[numero] = nodo
        
    def agregarArista(self, origen, destino, peso=1):
        self.nodos[origen].agregarAdyacente(self.nodos[destino], peso)
 
    def getNodo(self, numero):
        return self.nodos[numero]
 
 
    def __len__(self):
        return len(self.nodos)
 
    def __iter__(self):
        return iter(self.nodos.values())
        
    def existe(self, origen, destino):
        return self.nodos[origen].adyacente(self.nodos[destino])
 
 
 
class Nodo:
    def __init__(self, nro_nodo):
        self.nro_nodo = nro_nodo
        self.nodos_adyacentes = {}
 
    def get_key(self):
        return self.nro_nodo
 
    def agregarAdyacente(self, dest, peso):
        self.nodos_adyacentes[dest] = peso
 
    def getNodoAdyacentes(self):
        return self.nodos_adyacentes.keys()
 
    def peso(self, dest):
        return self.nodos_adyacentes[dest]
    
    def adyacente(self, dest):
        if dest in self.nodos_adyacentes:
            return True
        else:
            return False 
 
def bellman_ford(grafo, origen):
    distancia = dict.fromkeys(grafo, float('inf'))
    distancia[origen] = 0

    for _ in range(len(grafo) - 1):
        for nodo in grafo:
            for adyacente in nodo.getNodoAdyacentes():
                if int(nodo.peso(adyacente)) < 0 :
                    return 1
                distancia[adyacente] = min(distancia[adyacente], distancia[nodo] + int(nodo.peso(adyacente)))
                
    return distancia
   
    

 
def main():
    crearGrafo()  
    print("--- %s seconds ---" % (time.time() - start_time))
    

if __name__ == "__main__": main()
    