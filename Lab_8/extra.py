#2/3 - niepełne rozwiązanie
from typing import List
import random,time
from copy import deepcopy,copy
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



def shell_sort(lst,is_insertion = False):
    if is_insertion:
        n = 1
    else:
        n = len(lst) // 2

    while n >= 1:
        for i in range(n,len(lst)):

            elem = lst[i]
            j = i

            while j >= n and elem < lst[j - n]:
                lst[j] = lst[j - n]
                j -= n
            lst[j] = elem
        n //= 2


def insertionSort(lst):

    for i in range(1, len(lst)):

        key = lst[i]

        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def quicksort(data_input):
    def quicksort_inplace(data_input,start,stop):
        i = start
        j = stop
        pivot = data_input[start]
        while i < j:
            while data_input[j] > pivot:
                j -= 1
            while data_input[i] < pivot:
                i += 1
            if i <= j:
                data_input[i], data_input[j] = data_input[j], data_input[i]
                j -= 1
                i += 1
        if start < j:
            quicksort_inplace(data_input, start, j)
        if i < stop:
            quicksort_inplace(data_input, i, stop)
        return data_input

    data_input_copy = deepcopy(data_input)
    return quicksort_inplace(data_input_copy,0,len(data_input_copy) - 1)


def main():
    random_list = []
    check_list = [random.randint(0,10) for _ in range(10)]
    check_list_copy = deepcopy(check_list)
    check_list_2 = deepcopy(check_list)
    check_list_3 = deepcopy(check_list)
    random_list = [random.randint(0,1000) for _ in range(10000)]
    random_list_2 = deepcopy(random_list)
    random_list_3 = deepcopy(random_list)
    random_list_4 = deepcopy(random_list)
    shell_sort(check_list)
    shell_sort(check_list_2,is_insertion=True)
    check_list_3 =  quicksort(check_list_3)
    print(f'Tablica początkowa:\n{check_list_copy}')
    print(f'Tablica po uzyciu Shell sort:\n{check_list}')
    print(f'Tablica po uzyciu Insertion sort:\n{check_list_2}')
    print(f'Tablica po uzyciu quicksort:\n{check_list_3}')



    start = time.time()
    shell_sort(random_list)
    stop = time.time()
    print(f'Czas sortowania 10000 liczb dla algorytmu shell sort : {stop - start}\n\n')

    start = time.time()
    shell_sort(random_list_2,is_insertion=True)
    stop = time.time()
    print(f'Czas sortowania 10000 liczb dla algorytmu insertion  : {stop - start}\n\n')

    random_heap = Piority_queue(random_list_3)
    random_heap.heapify()
    start = time.time()
    while random_heap.dequeue() is not None:
        random_heap.dequeue()
    stop = time.time()
    print(f'Czas sortowania 10000 liczb dla algorytmu heapsort to: {stop - start}\n\n')

    start = time.time()
    random_list_4 = quicksort(random_list_4)
    stop = time.time()
    print(f'Czas sortowania 10000 liczb dla algorytmu quicksort : {stop - start}\n\n')



if __name__ == '__main__':
    main()

