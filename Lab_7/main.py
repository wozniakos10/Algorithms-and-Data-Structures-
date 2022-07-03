#5/5
import polska
from itertools import dropwhile

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
        self.list_of_vertex.append(vertex)
        self.dict_vert[vertex] = len(self.list_of_vertex) - 1
        self.adjacency_matrix.append([0] * (len(self.list_of_vertex) - 1))  #adding row with 0, size one less than amount of elements
        for k,v in enumerate(self.adjacency_matrix):
            self.adjacency_matrix[k].append(0)                  #For every row add 0 to make it equal to number elem


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

    def neighbours(self,vertex_id):
        pass

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

    def neighbours(self,vertex):
        idx = self.getVertexidx(vertex)
        value = []
        for k,v in enumerate(self.adjacency_matrix[idx]):
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
            if k > idx:         #If key bigger than delete : decrement
                self.neigh_list[k-1] = self.neigh_list.pop(k)       #deceremnet key

            while idx in v:
                v.pop(v.index(idx))              #deleting vertex from others neigohbour

            for elem,value in enumerate(v):
                if value > idx:  # if elem bigger than delete: decrement
                    v[elem] -= 1

        for key in dropwhile(lambda k: k != vertex, sorted(self.dict_vert, key=lambda x: self.dict_vert[
            x])):  # decrement index value after delete
            self.dict_vert[key] -= 1  # Prevent starting form deleting vertex

        self.dict_vert.pop(vertex)  # deleting vertex from dict




    def insertEdge(self,vertex1,vertex2,edge):
        idx1 = self.getVertexidx(vertex1)
        idx2 = self.getVertexidx(vertex2)
        self.neigh_list[idx1].append(idx2)

    def deleteEdge(self,vertex1, vertex2):
        idx1 = self.getVertexidx(vertex1)
        idx2 = self.getVertexidx(vertex2)
        self.neigh_list[idx1].remove(idx2)


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


    def edges(self):
        list_of_edges = []
        for k,v in self.neigh_list.items():         #Iterating trough neigh_list
            for elem in v:
                vert1 = self.getVertex(k)           #Getting vertex from idx
                vert2 = self.getVertex(elem)
                list_of_edges.append((vert1.key,vert2.key))         #Adding tupple to score

        return list_of_edges

    def size(self):
        value = 0
        for k,v in self.neigh_list.items():
            value += len(v)
        return value

    def neighbours(self,vertex):
        value = []
        idx = self.getVertexidx(vertex)
        for v in self.neigh_list[idx]:
            value.append(v)
        return value






def neigh_list_plot():
    a = Graphlist()

    for k in polska.polska:
        a.insertVertex(Vertex(k[2]))

    for k in polska.graf:
        v1 = a.get_vert_from_key(k[0])
        v2 = a.get_vert_from_key(k[1])
        a.insertEdge(v1, v2, Edge(1))

    a.deleteVertex(a.get_vert_from_key('K'))
    a.deleteEdge(a.get_vert_from_key('W'), a.get_vert_from_key('E'))
    a.deleteEdge(a.get_vert_from_key('E'), a.get_vert_from_key('W'))
    polska.draw_map(a.edges())

#neigh_list_plot()

def adj_matr_plot():
    a = Graphmat()

    for k in polska.polska:
        a.insertVertex(Vertex(k[2]))

    for k in polska.graf:
        v1 = a.get_vert_from_key(k[0])
        v2 = a.get_vert_from_key(k[1])
        a.insertEdge(v1,v2,Edge(1))

    a.deleteVertex(a.get_vert_from_key('K'))
    a.deleteEdge(a.get_vert_from_key('W'), a.get_vert_from_key('E'))
    a.deleteEdge(a.get_vert_from_key('E'), a.get_vert_from_key('W'))

    polska.draw_map(a.edges())

adj_matr_plot()
