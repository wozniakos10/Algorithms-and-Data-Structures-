#5/5
#Skończone
import numpy as np
import math
from itertools import dropwhile
from typing import List, NamedTuple, Union
import math
from copy import deepcopy


class Vertex:
    def __init__(self,key):
        self.key = key
        self.color = None

    def __eq__(self,other):
        return self.key == other.key


    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return f'Węzeł o kluczu {self.key}'

    def __repr__(self):
        return f'Klucz {self.key}'




class Edge:
    def __init__(self,weight,is_residual):
        self.weight = weight
        self.is_residual = is_residual
        self.flow = 0
        self.residual = weight

    def __repr__(self):
        return f'{self.weight} -- {self.flow} -- {self.residual} -- {self.is_residual}'



class Graphlist:
    def __init__(self):
        self.list_of_vertex = []
        self.dict_vert = {}
        self.neigh_list= {}

    def insertVertex(self,vertex):
        if vertex in self.list_of_vertex:
            pass
        else:
            self.list_of_vertex.append(vertex)          #Adding to vertex list
            self.dict_vert[vertex] = len(self.list_of_vertex) - 1       #Value of index
            self.neigh_list[self.dict_vert[vertex]] = []        #adding key and value to neigh_list

    def deleteVertex(self,vertex):
        idx = self.getVertexidx(vertex)
        self.list_of_vertex.pop(idx)

        self.neigh_list.pop(idx)

        for k ,v in self.neigh_list.copy().items():         #operating on copy to avoid runtime error
            if k > idx:                             #If key bigger than delete : decrement
                self.neigh_list[k-1] = self.neigh_list.pop(k)       #deceremnet key

        for k, v in self.neigh_list.copy().items():
            for i,j in enumerate(v):                    #Checking neghbours of vertex in beigh list
                if j[0] == idx:
                                                                #if it was vertex to delete - delete
                    self.neigh_list[k].remove([j[0],j[1]])


                elif j[0] > idx:                        #If index was bigger --- increment
                    j[0] -= 1

            # while idx in v:
            #     v.pop(v.index(idx))              #deleting vertex from others neigohbour

            # for elem,value in enumerate(v):
            #     if value > idx:  # if elem bigger than delete: decrement
            #         v[elem] -= 1

            # for k2,v2 in enumerate(v):
            #     pass


        for key in dropwhile(lambda k: k != vertex, sorted(self.dict_vert, key=lambda x: self.dict_vert[
            x])):  # decrement index value after delete
            self.dict_vert[key] -= 1  # Prevent starting form deleting vertex

        self.dict_vert.pop(vertex)  # deleting vertex from dict




    def insertEdge(self,vertex1,vertex2,edge):

        idx1 = self.getVertexidx(vertex1)
        idx2 = self.getVertexidx(vertex2)
        self.neigh_list[idx1].append([idx2,edge])

    def deleteEdge(self,vertex1, vertex2):
        idx1 = self.getVertexidx(vertex1)
        idx2 = self.getVertexidx(vertex2)
        for k,v in enumerate(self.neigh_list[idx1]):
            if v[0] == idx2:
                self.neigh_list[idx1].remove(v)



    def getVertexidx(self,vertex):
        return self.dict_vert[vertex]

    def getVertex(self,idx):
        return self.list_of_vertex[idx]

    def order(self):
        return len(self.list_of_vertex)

    def get_vert_from_key(self,key):
        for k,v in enumerate(self.list_of_vertex):
            if v.key == key:
                return v
        return False


    def edges(self):
        list_of_edges = []
        for k,v in self.neigh_list.items():         #Iterating trough neigh_list
            for elem in v:
                vert1 = self.getVertex(k)           #Getting vertex from idx
                vert2 = self.getVertex(elem[0])
                list_of_edges.append((vert1.key,vert2.key))         #Adding tupple to score

        return list_of_edges


    def size(self):
        value = 0
        for k,v in self.neigh_list.items():
            value += len(v)
        return value

    def neighbours(self, vertex,is_vertex = False):
        if is_vertex: #Checking if vertex was given or idx
            return self.neigh_list[self.getVertexidx(vertex)]

        return self.neigh_list[vertex]



def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j), f'waga = {w} ', end=": ")
        print()
    print("-------------------")





def initialize_graph(graph: Graphlist, vertex_list):            #Wczytywanie grafu

    for elem in vertex_list:
        vertex1 = Vertex(elem[0])
        vertex2 = Vertex(elem[1])
        graph.insertVertex(vertex1)
        graph.insertVertex(vertex2)
        graph.insertEdge(vertex1,vertex2,Edge(elem[2],is_residual=False))
        edge = Edge(elem[2],is_residual=True)
        edge.residual = 0
        graph.insertEdge(vertex2,vertex1,edge)



def bfs(graph:Graphlist,start_vertex: Vertex):
    visited = [False for _ in range(graph.order())]
    parrent = {}        #Pomocniczy slownik, w ktorym zapisuje rodzicow danycyh wierzcholkow
    value = []
    quoue = []

    vertex_idx = graph.getVertexidx(start_vertex)
    quoue.append(vertex_idx)
    visited[vertex_idx] = True
    value.append(start_vertex)
    while quoue:
        elem = quoue.pop(0)
        neigh = graph.neighbours(elem)

        for i in neigh:


            if visited[i[0]] is False and i[1].residual > 0:
                quoue.append(i[0])
                value.append(graph.getVertex(i[0]))
                parrent[graph.getVertex(i[0])] = graph.getVertex(elem)
                visited[i[0]] = True

    return value,parrent




def mini_value(graph: Graphlist, start_vertex: Vertex, end_vertex: Vertex,value: List, parrent):


    if end_vertex in value:
        act_idx = value.index(end_vertex)       #indeks aktualnego wierzcholka
        act_vertex = end_vertex     #aktualny wierzcholek
        maxi = math.inf
        while True:
            par_vertex = parrent[act_vertex]            #Znajdowanie rodzica w pomocnicznym slowniku

            for elem in graph.neigh_list[graph.getVertexidx(par_vertex)]:           #Znajdowanie w rodzicu krawedzi prowadzacej do aktaulnego

                if elem[0] == graph.getVertexidx(value[act_idx]) and not elem[1].is_residual:   #znajdowanie odpowiedniej rzeczywsitej krawedzi
                    edge = elem[1]  #przypisanie krawedzi

            if maxi > edge.residual:        #czy przepłyew resztowy jest mniejszny od najmniejszego znalezionego dotychczas
                maxi = edge.residual        #jesli tak to aktualizujeny

            act_vertex = par_vertex
            act_idx = value.index(act_vertex)       #aktualizacja wierzcholkow


            if act_idx == 0:            #Jezeli doszlismy do poczatku - zwroc wynik
                return maxi


    return 0


def augment(graph: Graphlist, start_vertex: Vertex, end_vertex: Vertex, value: List, minimal, parrent):
    act_idx = value.index(end_vertex)
    act_vertex = end_vertex
    while True:
        par_vertex = parrent[act_vertex]

        for elem in graph.neigh_list[
            graph.getVertexidx(par_vertex)]:  # Znajdowanie krawedzi od rodzica do wezla
            if elem[0] == graph.getVertexidx(value[act_idx]) and not elem[1].is_residual:
                real_edge = elem[1]

        for elem in graph.neigh_list[
            graph.getVertexidx(value[act_idx])]:  # Znajdowanie krawedzi od wezla do rodzica
            if elem[0] == graph.getVertexidx(par_vertex) and elem[1].is_residual:
                rest_edge = elem[1]
        real_edge.flow += minimal
        real_edge.residual -= minimal
        rest_edge.residual += minimal

        act_idx = value.index(par_vertex)
        act_vertex = par_vertex


        if act_idx == 0:
            break


    pass

def ford_fulkerson(graph: Graphlist,start_vertex: Vertex, end_vertex: Vertex):
    value,parrent = bfs(graph,start_vertex)
    if end_vertex in value:
        suma = 0
        minimal = mini_value(graph,start_vertex,end_vertex,value,parrent)
        suma += minimal
        while minimal > 0:
            augment(graph,start_vertex,end_vertex,value,minimal,parrent)
            value,parrent = bfs(graph,start_vertex)
            minimal = mini_value(graph,start_vertex,end_vertex,value,parrent)
            suma += minimal

        return suma

    print('Nie występuje ścieżka pomiędzy zadanymi wierzchołkami')


def main():


    graph_0 = Graphlist()
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    initialize_graph(graph_0,graf_0)

    graph_1 = Graphlist()
    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    initialize_graph(graph_1,graf_1)

    graph_2 = Graphlist()
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    initialize_graph(graph_2,graf_2)

    graph_3 = Graphlist()
    graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]
    initialize_graph(graph_3,graf_3)

    suma_0 = ford_fulkerson(graph_0,Vertex('s'),Vertex('v'))
    print('Graf 1:')
    print(f'Znaleziony przepływ: {suma_0}')
    print('Graf po operacji przepływu:')
    printGraph(graph_0)


    suma_1 = ford_fulkerson(graph_1,Vertex('s'),Vertex('t'))
    print('Graf 2:')
    print(f'Znaleziony przepływ: {suma_1}')
    print('Graf po operacji przepływu:')
    printGraph(graph_1)


    suma_2 = ford_fulkerson(graph_2,Vertex('s'),Vertex('t'))
    print('Graf 3:')
    print(f'Znaleziony przepływ: {suma_2}')
    print('Graf po operacji przepływu:')
    printGraph(graph_2)

    suma_3 = ford_fulkerson(graph_3,Vertex('s'),Vertex('t'))
    print('Graf 4:')
    print(f'Znaleziony przepływ: {suma_3}')
    print('Graf po operacji przepływu:')
    printGraph(graph_3)


if __name__ == '__main__':
    main()