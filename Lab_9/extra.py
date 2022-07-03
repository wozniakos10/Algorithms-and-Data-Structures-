#2/2
import copy
import cv2
import matplotlib.pyplot as plt
import numpy as np
#Skończone
from itertools import dropwhile
from  graf_mst import graf
from typing import List, NamedTuple, Union
import math
from copy import deepcopy


class Vertex:
    def __init__(self,key,color):
        self.key = key
        self.color = color

    def __eq__(self,other):
        return self.key == other.key


    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return f'Węzeł o kluczu {self.key}'

    def __repr__(self):
        return f'Klucz {self.key}'




class Edge:
    def __init__(self,weight):
        self.weight = weight




class Graphlist:
    def __init__(self):
        self.list_of_vertex = []
        self.dict_vert = {}
        self.neigh_list= {}

    def insertVertex(self,vertex):
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
        self.neigh_list[idx1].append([idx2,edge.weight])

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





def prim_mst(G: Graphlist,s):
    intree = {}
    distance = {}
    parent = {}
    for elem in G.list_of_vertex:
        intree[elem] = 0                #Initializaiton of helplful varaible
        distance[elem] = math.inf
        parent[elem] = - 1
    mst_tree = Graphlist()
    for elem in G.list_of_vertex:

        mst_tree.insertVertex(deepcopy(elem))       #Creating mst with olny vertex

    v = s       #Current vertex
    sum_tree = 0
    while True:
        intree[v] = 1       #Adding current vertex to mst
        for elem in G.neighbours(v,is_vertex=True):
            if elem[1] < distance[G.getVertex(elem[0])] and intree[G.getVertex(elem[0])] == 0 :     #if wegiht is loweer than in distance and vertex not in mst
                distance[G.getVertex(elem[0])] = elem[1]        #Update distance
                parent[G.getVertex(elem[0])] = v                #Set parrents of find vertex as current vertex


        dist = math.inf
        for elem in G.list_of_vertex:           #Looking for new vertex
            if intree[elem] == 0 and dist > distance[elem]:   #IF vertex has lowwer weight and not in mst
                dist = distance[elem]                   #Update distance(weight)
                v = elem                            #Update current elem

        if intree[v] == 1:          #If new find vertex is on mst - it means there are no more vertex - break
            break



        mst_tree.insertEdge(v,parent[v],Edge(dist))         #Adding edge to mst A->B
        mst_tree.insertEdge(parent[v],v, Edge(dist))        #Adding edge to mst B->A
        sum_tree += dist        #Updating sum


    return mst_tree,sum_tree






I = cv2.imread('sample.png',cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(I,'gray')
plt.axis('off')
plt.show()
graph = Graphlist()


YY = len(I)

for k,v in enumerate(I):
    for k2,v2 in enumerate(v):
        vert = Vertex(YY * k2 + k,color=v2)
        graph.insertVertex(Vertex(YY * k2 + k,color=v2)) #Tworzenie wierzcholkow



for r in range(1,YY - 1):
    for c in range(1,YY - 1):
        neigh_1 = I[r-1,c-1]        #Wstawianie krawedzi
        neigh_2 = I[r - 1, c]
        neigh_3 = I[r - 1, c + 1]
        neigh_4 = I[r, c - 1]
        neigh_5 = I[r, c + 1]
        neigh_6 = I[r + 1, c + 1]
        neigh_7 = I[r + 1, c]
        neigh_8 = I[r + 1, c - 1]
        vert = graph.get_vert_from_key(YY * c + r)
        vert1 = graph.get_vert_from_key(YY * (c-1) + r - 1)
        vert2 = graph.get_vert_from_key(YY * c + r - 1)
        vert3 = graph.get_vert_from_key(YY * (c+1) + r - 1)
        vert4 = graph.get_vert_from_key(YY * (c-1) + r)
        vert5 = graph.get_vert_from_key(YY * (c+1) + r)
        vert6 = graph.get_vert_from_key(YY * (c+1) + r + 1)
        vert7 = graph.get_vert_from_key(YY * c + r + 1)
        vert8 = graph.get_vert_from_key(YY * (c-1) + r +1 )

        graph.insertEdge(vert,vert1,Edge(weight=np.abs(int(I[r,c]) - int(neigh_1))))
        graph.insertEdge(vert, vert2, Edge(weight=np.abs(int(I[r,c]) - int(neigh_2))))
        graph.insertEdge(vert, vert3, Edge(weight=np.abs(int(I[r,c]) - int(neigh_3))))
        graph.insertEdge(vert, vert4, Edge(weight=np.abs(int(I[r,c]) - int(neigh_4))))
        graph.insertEdge(vert, vert5, Edge(weight=np.abs(int(I[r,c]) - int(neigh_5))))
        graph.insertEdge(vert, vert6, Edge(weight=np.abs(int(I[r,c]) - int(neigh_6))))
        graph.insertEdge(vert, vert7, Edge(weight=np.abs(int(I[r,c]) - int(neigh_7))))
        graph.insertEdge(vert, vert8, Edge(weight=np.abs(int(I[r,c]) - int(neigh_8))))



mst_value,sum_mst = prim_mst(graph,graph.get_vert_from_key(232))

max_weight = 0


for key,item in mst_value.neigh_list.items():
    for elem in item:
        if elem[1] > max_weight:        #Szukanie krawedzi o najwiekszej wadze
            max_weight = elem[1]
            vert_2_idx = elem[0]
            vert_1_idx = key

#Usuniecie krawedzi o najwiekszej wadze
mst_value.deleteEdge(mst_value.getVertex(vert_2_idx),mst_value.getVertex(vert_1_idx))




IS = np.zeros((32,32),dtype='uint8')


def bfs(graph:Graphlist,start_vertex: Vertex):
    visited = [False for _ in range(graph.order())]
    parrent = []
    quoue = []

    vertex_idx = graph.getVertexidx(start_vertex)
    quoue.append(vertex_idx)
    visited[vertex_idx] = True
    parrent.append(graph.getVertex(vertex_idx))

    while quoue:
        elem = quoue.pop(0)
        neigh = graph.neighbours(elem)

        for i in neigh:

            if visited[i[0]] is False:

                quoue.append(i[0])
                parrent.append(graph.getVertex(i[0]))
                visited[i[0]] = True


    return parrent

first_neigh = bfs(mst_value,mst_value.getVertex(vert_1_idx))  #2 czesci obrazka
second_neigh = bfs(mst_value,mst_value.getVertex(vert_2_idx))


for elem in first_neigh:
    elem.color = 150            #Ustawianie kolorow dla obu czesci

for elem in second_neigh:
    elem.color = 220

for k,v in enumerate(I):
    for k2,v2 in enumerate(v):
            #Przypisywanie obrazkowi odpowiednich,wczesniej ustawionych kolorow
        IS[k,k2] = mst_value.get_vert_from_key(YY * k2 + k).color


plt.figure()
plt.imshow(IS,'gray',vmin=0,vmax=255)
plt.axis('off')
plt.show()
