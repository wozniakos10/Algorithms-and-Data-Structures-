# 5/5
from itertools import dropwhile
import numpy as np
from copy import deepcopy
#Skończone


class Vertex:
    def __init__(self,key):
        self.key = key

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
        if vertex not in self.list_of_vertex:

            self.list_of_vertex.append(vertex)
            self.dict_vert[vertex] = len(self.list_of_vertex) - 1
            self.adjacency_matrix.append([0] * (len(self.list_of_vertex) - 1))
            for k,v in enumerate(self.adjacency_matrix):
                self.adjacency_matrix[k].append(0)
        else:
            pass

    def insertEdge(self,vertex1,vertex2,edge):
        self.adjacency_matrix[self.dict_vert[vertex1]][self.dict_vert[vertex2]] += 1


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
        if self.adjacency_matrix[self.dict_vert[vertex1]][self.dict_vert[vertex2]] > 0:
            self.adjacency_matrix[self.dict_vert[vertex1]][self.dict_vert[vertex2]] -= 1

    def getVertexidx(self,vertex):
        return self.dict_vert[vertex]

    def getVertex(self,vertex_idx):
        return self.list_of_vertex[vertex_idx]

    def neighbours(self,vertex_idx):
        neigh = []
        for i in range(0,len(self.adjacency_matrix[vertex_idx])):
            if self.adjacency_matrix[i] == 1:
                neigh.append(i)
        return neigh

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
        for k,v in enumerate(self.list_of_vertex):
            if v.key == key:
                return v

    def neighbours(self,vertex,is_vertex = False):
        if is_vertex:
            vertex = self.getVertexidx(vertex)
        value = []
        for k,v in enumerate(self.adjacency_matrix[vertex]):
            if v != 0:
                value.append(k)
        return value

    def get_adjacency_matrix(self):
        return np.array(self.adjacency_matrix,dtype='int')



def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v, end = " -> ")
        nbrs = g.neighbours(i)
        for j in nbrs:
            print(g.getVertex(j),end=": ")
        print()
    print("-------------------")




def initialize_graph(graph: Graphmat, vertex_list):            #Wczytywanie grafu

    for elem in vertex_list:
        vertex1 = Vertex(elem[0])
        vertex2 = Vertex(elem[1])
        graph.insertVertex(vertex1)
        graph.insertVertex(vertex2)
        graph.insertEdge(vertex1,vertex2,Edge(1))
        edge = Edge(1)
        graph.insertEdge(vertex2,vertex1,edge)


class Ulman_counter:
    def __init__(self):
        self.count = 0
        self.times = 0

    def __call__(self,value=True):
        if value:
            self.count += 1
        else:
            self.times += 1



def prune(M,P: Graphmat,G: Graphmat):
    flag = True
    while flag:
        flag = False
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                if M[i, j] == 1:
                    p_neigh = P.neighbours(i)
                    g_neigh = G.neighbours(j)


                    for x in range(0, P.get_adjacency_matrix().shape[0]):
                        for y in range(0, G.get_adjacency_matrix().shape[1]):
                            if M[x, y] == 1:
                                flag_2 = True
                                break

                    if not flag_2:
                        M[i, j] = 0

                        flag = True

                        break




def ullman(G, P, M,counter):
    #inicjalizacja kolumn
    start_lst = [False for _ in range(M.shape[1])]

    def ullman_inplace(used_columns, current_row, G, P, M, counter):
        #Zwiekszenie ilosci wywolan
        counter(value=False)
        #Warunek koncowy
        if current_row == len(M):
            multip = np.dot(M,G)
            cond = np.dot(M,np.transpose(multip))
            #Sprawdzenie warunku mnozenia macierzowego
            if (P == cond).all():
                #Zwiekszenie ilosci znalezionych izomorfizmow
                counter()

            return False

        M_copy = deepcopy(M)
        for i in range(M_copy.shape[1]):
            if not used_columns[i]:
                #dla wszytich kolumn
                for col in range(M_copy.shape[1]):
                    #ustawianie nieuzywanych kolumn na 1
                    if col == i:
                        M_copy[current_row][col] = 1
                    else:
                        M_copy[current_row][col] = 0

                #zaznaczenie jako uzywane
                used_columns[i] = True
                #rekurencja
                ullman_inplace(used_columns, current_row+1, G,P, M_copy,counter)
                #zaznaczone jako nieuzywane
                used_columns[i] = False
        return False

    return ullman_inplace(start_lst, 0, G, P, M,counter)

def ullman2(G, P, M,counter,M0):
    #inicjalizacja kolumn
    start_lst = [False for _ in range(M.shape[1])]

    def ullman_inplace(used_columns, current_row, G, P, M, counter,M0):
        #Zwiekszenie ilosci wywolan
        counter(value=False)
        #Warunek koncowy
        if current_row == len(M):
            multip = np.dot(M,G)

            cond = np.dot(M,np.transpose(multip))
            #Sprawdzenie warunku mnozenia macierzowego
            if (P == cond).all():
                #Zwiekszenie ilosci znalezionych izomorfizmow
                counter()

            return False

        M_copy = deepcopy(M)
        for i in range(M_copy.shape[1]):
            if not used_columns[i]:
                #dla wszytich kolumn
                #Dodatowy waurnek przyspieszajacy M1
                if M0[current_row][i] == 1:
                    for col in range(M_copy.shape[1]):
                        #ustawianie nieuzywanych kolumn na 1
                        if col == i:
                            M_copy[current_row][col] = 1
                        else:
                            M_copy[current_row][col] = 0

                    #zaznaczenie jako uzywane
                    used_columns[i] = True
                    #rekurencja
                    ullman_inplace(used_columns, current_row+1, G,P, M_copy,counter,M0)
                    #zaznaczone jako nieuzywane
                    used_columns[i] = False
        return False

    return ullman_inplace(start_lst, 0, G, P, M,counter,M0)



def ullman3(G, P, M,counter,M0):
    #inicjalizacja kolumn
    start_lst = [False for _ in range(M.shape[1])]

    def ullman_inplace(used_columns, current_row, G, P, M, counter,M0):
        #Zwiekszenie ilosci wywolan
        counter(value=False)
        #Warunek koncowy
        if current_row == len(M):
            multip = np.dot(M,G.get_adjacency_matrix())
            cond = np.dot(M,np.transpose(multip))
            #Sprawdzenie warunku mnozenia macierzowego
            if (P.get_adjacency_matrix() == cond).all():
                #Zwiekszenie ilosci znalezionych izomorfizmow
                counter()


            return False

        M_copy = deepcopy(M)
        prune(M_copy,P,G)

        for i in range(M_copy.shape[1]):
            if not used_columns[i]:
                #dla wszytich kolumn
                #Dodatowy waurnek przyspieszajacy M1
                if M0[current_row][i] == 1:
                    for col in range(M_copy.shape[1]):
                        #ustawianie nieuzywanych kolumn na 1
                        if col == i:
                            M_copy[current_row][col] = 1
                        else:
                            M_copy[current_row][col] = 0

                    #zaznaczenie jako uzywane
                    used_columns[i] = True
                    #rekurencja
                    ullman_inplace(used_columns, current_row+1, G,P, M_copy,counter,M0)
                    #zaznaczone jako nieuzywane
                    used_columns[i] = False
        return False

    return ullman_inplace(start_lst, 0, G, P, M,counter,M0)







def main():
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

    graph_g = Graphmat()
    graph_p = Graphmat()
    initialize_graph(graph_g,graph_G)
    initialize_graph(graph_p,graph_P)



    #M generuj brute_forcem i sprawdzaj czy iloczyn jest spelniony
    graph_p_matrix = graph_p.get_adjacency_matrix()
    graph_g_matrix = graph_g.get_adjacency_matrix()
    M = np.zeros((graph_p.order(),graph_g.order()),dtype='int')

    M0 = np.zeros((graph_p.order(),graph_g.order()))

    for i in range(graph_p.order()):
        p_edges = len(graph_p.neighbours(i))
        for j in range(graph_g.order()):
            g_edges = len(graph_g.neighbours(j))
            if p_edges <= g_edges:
                M0[i, j] = 1

    first = Ulman_counter()
    second = Ulman_counter()
    third = Ulman_counter()



    ullman(graph_g_matrix,graph_p_matrix,M,first)
    ullman2(graph_g_matrix,graph_p_matrix,M,second,M0)
    ullman3(graph_g, graph_p, M, third, M0)

    print(f'Wersja 1.0: Liczba znalezionych izomorfizmów: {first.count}, liczba wywołań funkcji: {first.times}')
    print(f'Wersja 2.0: Liczba znalezionych izomorfizmów: {second.count}, liczba wywołań funkcji: {second.times}')
    print(f'Wersja 3.0: Liczba znalezionych izomorfizmów: {third.count}, liczba wywołań funkcji: {third.times}')



x = [1,2,3,4,5]
print(x[-3:])