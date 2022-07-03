# 5/5

class Llist:
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        help_value = self.head
        self.head = data
        self.head.next = help_value

    def add_last(self, data):
        value = self.head
        if self.head is None:                #Kiedy lista jest pusta, ustaw head na data
            self.head = data

        else:
            while value.next is not None:           #Az next z ostatniego rozny od Nonne
                y = value.next
                value = y                           #Iteruj po kolekcji
            value.next = data                       #Ustaw next ostatniego Heada na wartość ktora ma byc dodana

    def remove_last(self):
        if self.head is None:
            pass

        elif self.head.next is not None:
            back_value = self.head                  #Wartości pomocnicze/ Docelowo przedostatnia wartosc

            forward_value = self.head.next              #Docelowo ostatnia wartosć

            while forward_value.next is not None:       #Aż next z ostatniej wartosci nie wskazuje na None
                back_value = forward_value                   #Itrowanie po kolekcji
                forward_value = forward_value.next

            back_value.next = None
        else:
            self.head = None                                                #Ustawienie nexta z przedostaniego elementu na None

    def destroy(self):
        self.head = None

    def remove(self):
        if self.head is not None:
            self.head = self.head.next

    def is_empty(self):
        if self.head is None:
            return True

    def length(self):
        counter = 0
        checking = self.head
        while checking is not None:
            y = checking.next
            checking = y               #Aż head rozny od None, zliczaj ilosci headow
            counter += 1
        return counter

    def get(self):
        return self.head.data

    def take(self, n):
        counter = 0
        value = self.head
        container = Llist()
        while counter < n and value is not None:
            container.add_last(Element(value.data))
            value = value.next
            counter += 1

        return container

    def drop(self, n):
        counter = 0
        value = self.head
        container = Llist()

        if n >= self.length():
            return container

        else:

            while counter < n and value.next is not None:
                value = value.next
                counter += 1



            if value is not None:
                container.add_last(Element(value.data))

            while value.next is not None:
                value = value.next
                container.add_last(Element(value.data))

            return container

    def __str__(self):
        x = self.head
        if x is None:
            return f'[]'
        s = f''
        while x:
            s += " " + f'{x.data}'
            x = x.next
        return s

class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


def main():
    llist = Llist()
    data = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]

    for k,v in enumerate(data):
        llist.add_last(Element(v))
    print(llist,'\n')
    print(f'Pierwszy element listy to: {llist.get()}\n')

    llist.remove_last()
    llist.add(Element(data[-1]))

    print(f'Lista po usunięciu ostatniego elementu i wstawieniu na początek:\n{llist}\n')

    llist.remove()
    llist.add_last(Element(data[-1]))



    print(f'Lista po usunięciu pierwszego elementu i wstawieniu go na koniec:\n{llist}\n')


    print(f'Ilość elementów w liście: {llist.length()}\n')

    take_list = llist.take(3)
    take2_list = llist.take(7)
    drop_list = llist.drop(4)
    drop2_list = llist.drop(7)
    print(f'Nowa lista powstała z 3 pierwszych elementów:\n{take_list}\n')

    print(f'Nowa lista powstała z pominięciem pierwszych 4 elementów:\n{drop_list}\n')

    print(f'Nowa lista powstała z 7 pierwszych elementów(czyli ma przypisać całą listę):\n{take2_list}\n')

    print(f'Nowa lista powstała z pominięciem pierwszych 7 elementów(czyli zwróci pustą listę):\n{drop2_list}\n')

    llist.destroy()

    print(f'Długość listy po usunięciu: {llist.length()}')

    print(f'Czy lista jest pusta? {llist.is_empty()}')




if __name__ == "__main__":
    main()

