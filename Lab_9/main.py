#5/5
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


class Graphmat:
    def __init__(self):
        self.list_of_vertex = []
        self.dict_vert = {}
        self.adjacency_matrix = []


    def insertVertex(self,vertex):
        self.list_of_vertex.append(vertex)
        self.dict_vert[vertex] = len(self.list_of_vertex) - 1
        for k,v in enumerate(self.adjacency_matrix):
            self.adjacency_matrix[k].append(0)                  #For every row add 0 to make it equal to number elem
        self.adjacency_matrix.append([0] * len(self.list_of_vertex))  #adding row with 0, size one less than amount of elements



    def insertEdge(self,vertex1,vertex2,edge):
        self.adjacency_matrix[self.dict_vert[vertex2]][self.dict_vert[vertex1]] += 1


    def deleteVertex(self,vertex):
        vertex_idx = self.dict_vert[vertex]     #idx of deleting vertex
        self.adjacency_matrix.pop(vertex_idx)   #deleting vertex form adjacency matrix
        for k,v in enumerate(self.adjacency_matrix):
            self.adjacency_matrix[k].pop(vertex_idx)                #In every list deleting column with vertex to delete
        self.list_of_vertex.pop(vertex_idx)     #Deleting vertex form dict


        for key in dropwhile(lambda k: k != vertex, sorted(self.dict_vert, key= lambda x: self.dict_vert[x])):    #decrement index value after delete

            self.dict_vert[key] -= 1


        self.dict_vert.pop(vertex)      #deleting vertex from dict

    def deleteEdge(self,vertex1,vertex2):
        self.adjacency_matrix[self.dict_vert[vertex1]][self.dict_vert[vertex2]] = 0

    def getVertexidx(self,vertex):
        return self.dict_vert[vertex]

    def getVertex(self,vertex_idx):
        return self.list_of_vertex[vertex_idx]


    def order(self):
        return len(self.list_of_vertex)

    def size(self):
        counter = 0

        for k, v in enumerate(self.adjacency_matrix):
            for k2,v2 in enumerate(v):
                if v2 != 0:
                    counter += 1

        return counter

    def edges(self):
        list_of_edges = []
        for k, v in enumerate(self.adjacency_matrix):
            for i in range(len(v)):
                if v[i] != 0:
                    list_of_edges.append((self.list_of_vertex[k].key, self.list_of_vertex[i].key))

        return list_of_edges

    def get_vert_from_key(self,key):
        return self.list_of_vertex[self.dict_vert[key]]

    def neighbours(self, vertex):
        idx = self.getVertexidx(vertex)
        value = []
        for k, v in enumerate(self.adjacency_matrix[idx]):
            if v != 0:
                value.append(k)
        return value


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


def main():
    vert = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    graph = Graphlist()

    for elem in graf:
        if not graph.get_vert_from_key(elem[0]):
            graph.insertVertex(Vertex(elem[0]))

        if not graph.get_vert_from_key(elem[1]):
            graph.insertVertex(Vertex(elem[1]))

        idx1 = graph.get_vert_from_key(elem[0])
        idx2 = graph.get_vert_from_key(elem[1])

        graph.insertEdge(idx1, idx2, Edge(elem[2]))
        graph.insertEdge(idx2, idx1, Edge(elem[2]))



    mst,sum_mst = prim_mst(graph,Vertex('A'))
    printGraph(mst)
    print(f'Długość drzewa rozpinającego: {sum_mst}')

if __name__ == '__main__':
    main()