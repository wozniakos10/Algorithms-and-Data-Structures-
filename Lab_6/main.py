#5/5
# Skończone

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
    def __init__(self):
        self.tab = []


    def is_empty(self):
        if self.tab:
            return False

        else:
            return True

    def peek(self):

        if self.is_empty():
            return None

        return self.tab[0].data


    def dequeue(self):
        if self.is_empty():
            return None

        self.tab[0], self.tab[-1] = self.tab[-1], self.tab[0]
        value = self.tab.pop(-1).data
        idx = 0
        while True:

            if self.right(idx)  < len(self.tab):                  #Istnienie prawego dziecka

                if self.left(idx)  < len(self.tab):  # Istnienie obu dzieci

                    if self.tab[idx] < self.tab[self.right(idx)] or self.tab[idx] < self.tab[self.left(idx)]:   #Gdy istnieją dwa, zamień z większym
                        if self.tab[self.right(idx)] < self.tab[self.left(idx)]:
                            self.tab[idx], self.tab[self.left(idx)] = self.tab[self.left(idx)], self.tab[idx]       #Lewe większe - zamień lewe
                            idx = self.left(idx)    #Aktualizacja indeksow

                        else:
                            self.tab[idx], self.tab[self.right(idx)] = self.tab[self.right(idx)], self.tab[idx]     #Prawe większe - zamień prawe
                            idx = self.right(idx)   #Aktualizacja indeksow
                    else:       #Jeżeli żadne z dzieci nie jest większe - break
                        break

                else:
                    if self.tab[idx] < self.tab[self.left(idx)]:                                            #Gdy istnieje tylko lewe
                        self.tab[idx],self.tab[self.left(idx)] = self.tab[self.left(idx)], self.tab[idx]        #Jeśli trzeba to zamień
                        idx = self.right(idx)
                    else:
                        break               #Jeżeli nie jest większe - break




            else:
                break               #Jeśli nie ma już dzieci - break

        return value





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



def main():

    em = Piority_queue()
    x = [4, 7, 6, 7, 5, 2, 2, 1]
    b = 'ALGORYTM'

    for k,v in zip(x,b):
        em.enqueue(Element(k,v))

    em.print_tree(0,0)
    em.print_tab()
    print(em.dequeue())
    print(em.peek())
    em.print_tab()
    while not em.is_empty():
        em.dequeue()
    em.print_tab()

if __name__ == "__main__":
    main()