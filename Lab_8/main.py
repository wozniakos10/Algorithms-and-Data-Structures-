#5/5
# Skończone
from typing import List
import random,time
from copy import deepcopy
class Element:
    def __init__(self,piority, data):
        self.data = data
        self.piority = piority
        self.right = None
        self.left = None

    def __lt__(self, other):
        return self.piority < other.piority

    def __gt__(self, other):
        return self.piority > other.piority

    def __eq__(self, other):
        return  self.piority == other.piority

    def __repr__(self):
        return f'{self.piority} : {self.data}'


class Piority_queue:
    def __init__(self,tab = None):
        if tab is None:
            self.tab = []
            self.size = 0
        else:
            self.tab = tab
            self.size = len(self.tab)


    def is_empty(self):
        if not self.tab :
            return True

        else:
            return False

    def peek(self):

        if self.is_empty():
            return None

        return self.tab[0].data


    def dequeue(self):
        #TODO: nie usuwaj ostatniego elementu
        if self.is_empty() or self.size == 0:
            return None

        self.tab[0], self.tab[self.size - 1] = self.tab[self.size - 1], self.tab[0]

        self.size -= 1
        self.heap_from_tab_alg(0)


        return self.tab[self.size]


    def heapify(self):
        idx = self.parent(self.size)
        while idx !=-1:
            self.heap_from_tab_alg(idx)
            idx -= 1


    def heap_from_tab_alg(self,idx):
        while True:
            if self.right(idx) < self.size:  # Istnienie prawego dziecka

                if self.left(idx) < self.size:  # Istnienie obu dzieci

                    if self.tab[idx] < self.tab[self.right(idx)] or self.tab[idx] < self.tab[
                        self.left(idx)]:  # Gdy istnieją dwa, zamień z większym
                        if self.tab[self.right(idx)] < self.tab[self.left(idx)]:
                            self.tab[idx], self.tab[self.left(idx)] = self.tab[self.left(idx)], self.tab[
                                idx]  # Lewe większe - zamień lewe
                            idx = self.left(idx)  # Aktualizacja indeksow

                        else:
                            self.tab[idx], self.tab[self.right(idx)] = self.tab[self.right(idx)], self.tab[
                                idx]  # Prawe większe - zamień prawe
                            idx = self.right(idx)  # Aktualizacja indeksow
                    else:  # Jeżeli żadne z dzieci nie jest większe - break
                        return False

                else:
                    if self.tab[idx] < self.tab[self.left(idx)]:  # Gdy istnieje tylko lewe
                        self.tab[idx], self.tab[self.left(idx)] = self.tab[self.left(idx)], self.tab[
                            idx]  # Jeśli trzeba to zamień
                        idx = self.right(idx)
                    else:
                        return False   # Jeżeli nie jest większe - break




            else:
                return False  # Jeśli nie ma już dzieci - break

        return True





    def left(self, index):
        return index * 2 + 1


    def right(self, index):
        return index * 2 + 2


    def parent(self, index):
        return (index - 1) // 2

    def enqueue(self, elem):
        if self.is_empty():
            self.tab.append(elem)           #Jeśli kolejka była pusta, po prostu dodaj

        else:
            self.tab.append(elem)
            idx = self.parent(len(self.tab) - 1)                #indeks rodzica
            elem_indx = len(self.tab) - 1                       #indeks elementu

            while self.tab[elem_indx] > self.tab[idx]:              #kiedy elementy sie nie zgadzają

                if elem_indx == 0:                                #Jeżeli rodzic to pierwszy element - skończ
                    break

                self.tab[elem_indx], self.tab[idx] = self.tab[idx], self.tab[elem_indx]     #Zamień elementy
                elem_indx = idx                                                 #Zaaktualizuj indeksy
                idx = self.parent(elem_indx)

        self.size += 1


    def print_tab(self):
        if self.is_empty():
            print('{}')
        else:
            print('{', end=' ')
            for i in range(len(self.tab) - 1):
                print(self.tab[i], end=', ')
            if self.tab[len(self.tab) - 1]: print(self.tab[len(self.tab) - 1], end=' ')
            print('}')

    def print_tree(self, idx, lvl):
        if idx < len(self.tab):
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.tab[idx] if self.tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)

    def __str__(self):
        return f'{self.tab}'

def selection_sort(lst: List) -> None:

    for i in range(len(lst)):
        min_idx = i
        for j in range(i,len(lst)):
            if lst:
        if  i != min_idx:
            lst[i],lst[min_idx] = lst[min_idx],lst[i]


def selection_sort_shift(lst:List) -> None:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j

        if i != min_idx:
            x = lst.pop(min_idx)
            lst.insert(i,x)









def test():
    help_lst = [(5, 'A'), (5, 'B'), (7, 'C'), (2, 'D'), (5, 'E'), (1, 'F'), (7, 'G'), (5, 'H'), (1, 'I'), (2, 'J')]
    lst = []
    for elem in help_lst:
        lst.append(Element(elem[0], elem[1]))
    lst_2 = deepcopy(lst)
    lst_3 = deepcopy(lst)

    random_list = []
    for i in range(10000):
        random_list.append(random.randint(0, 1000))
    random_list_2 = deepcopy(random_list)
    random_list_3 = deepcopy(random_list)

    heap_list = Piority_queue(lst)
    heap_list.heapify()

    while heap_list.dequeue() is not None:
        heap_list.dequeue()
    print(f'Zadana tablica dla sortowania heapsort:\n{heap_list.tab}')
    print('Algorytm heapsort nie jest stabilny')
    # Algorytm nie jest stabilny, widać element (1,'F') oraz (1,'I') zamienily sie miejscami

    random_heap = Piority_queue(random_list)
    random_heap.heapify()
    start = time.time()
    while random_heap.dequeue() is not None:
        random_heap.dequeue()
    stop = time.time()
    print(f'Czas sortowania 10000 liczb dla algorytmu heapsort to: {stop - start}\n\n')

    #------------------Selection_______________________------------------
    selection_sort(lst_2)

    print(f'Zadana tablica dla sortowania selection ze swapem:\n{lst_2}')
    print('Algorytym selection ze swapem nie jest stabilny')


    start = time.time()
    selection_sort(random_list_2)
    stop = time.time()
    print(f'Czas sortowania 10000 liczb dla algorytmu selection sort z swapem to: {stop - start}\n\n')

    selection_sort_shift(lst_3)
    # Algorytm selection z metodą swap nie jest stabilny.
    print(f'Zadana tablica dla sortowania selection ze shiftem:\n{lst_3}')
    print('Algorytym selection ze shiftem  jest stabilny')

    start = time.time()
    selection_sort_shift(random_list_3)

    stop = time.time()
    print(f'Czas sortowania 10000 liczb dla algorytmu selection sort z shiftem to: {stop - start}')


def main():
    test()


main()

