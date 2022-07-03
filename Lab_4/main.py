# 5/5
from copy import deepcopy
class NotFoundError(Exception):
    def __init__(self,key):
        self.key = key
        super().__init__(f'Element o kluczu {self.key} nie występuje w tablicy')

class InsertError(Exception):
    def __init__(self):
        super().__init__(f'Brak miejsca w tablicy! nie można wstawić tego elementu')


class Hashtable:
    def __init__(self,size,*,c1 = 1,c2 = 0):
        self.size = size
        self.tab = [None for i in range(self.size)]
        self.c1 = c1
        self.c2 = c2

    def mix(self,data):
        """Funkcja haszująca"""
        if isinstance(data,str):
            x = 0
            for key,value in enumerate(data):
                if value != "":
                    x += ord(value)

            return x % self.size
        else:
            return data % self.size

    def overlap(self,data):
        """Radzenie sobie z kolizją"""
        help = deepcopy(data)
        flag  = False
        for k,v in enumerate(self.tab):
            if v is None:
                flag = True
                break

        if flag:

            i = 1
            while self.tab[data] is not None:

                data = ( help + self.c1*i + self.c2*i ** 2 ) % self.size
                i += 1

                if i > 10000* self.size:
                    raise InsertError
                                                        #Rzucenie wyjątku, gdy nie da sie wsatwic elementu
        else:
            raise InsertError


        return data

    def search_overloap(self,place,data):
        help = deepcopy(place)
        i =  0
        while True:
            place = (help + self.c1 * i + self.c2 * i ** 2) % self.size
            i += 1                                                                  #Radzenie sobie z mozliwa byla kolizja przy wyszukiwaniu i usuwaniu
            if self.tab[place] is not None:
                if self.tab[place].key == data:
                    return place

            if i > self.size :
                raise NotFoundError(data)

        return place

    def search(self,data):
        """Wyszukiwanie elementu"""
        place = self.mix(data)
        if self.tab[place] is not None:                             #Jezeli elemennt pod hashem nie jest Nonem
            if self.tab[place].key == data:
                return self.tab[place].value                        #Jezeli klucze sie zgadzaj to zwroc element
            else:
                try:
                    place = self.search_overloap(place, data)
                    return self.tab[place].value                        #Else szukaj elementu, jesli sie nie znajdzie to rzucany jest wyujatek

                except NotFoundError:
                    print('Zadany element nie występuje')

        else:
            try:
                place = self.search_overloap(place,data)
                return self.tab[place].value                                #Przypadek gdy element pod obliczonym hashem byl nonem
                                                                            #czyli pierwoytny element z danym hashem zostal usuniety, a element ktory my chcemy usunac zostal obsluzony kolizja
            except NotFoundError:                                         #Jesli sie nie uda znalezc to rzuca wyjatek
                print('Zadany element nie występuje')



        return None

    def insert(self,data):
        """Wstawianie elementu do tablicy"""
        place = self.mix(data.key)
        if self.tab[place] is not None:
            if self.tab[place].key == data.key:             #Nadpisywanie klucza w słowniku
                self.tab[place].value = data.value
            else:
                try:
                    place = self.overlap(place)          #Radzenie sobie z kolizją
                    self.tab[place] = data
                except InsertError:
                    print("Brak miejsca w tablicy")
        else:
            self.tab[place] = data


    def remove(self,data):

        place = self.mix(data)
        if self.tab[place] is not None:
            if self.tab[place].key == data:
                self.tab[place] = None
            else:                                                       #Przypadek jesli element pod otrzymanym hashem nie jest nonem
                try:                                                    #Jezeli klucze sie zgadzaja to usun,a w przeciwnym przypadku szukaj tego elementu
                    place = self.search_overloap(place, data)           #Jezeli sie nie uda rzucany jesy wyjatek
                    self.tab[place] = None

                except NotFoundError:
                    print('Zadany element nie występuje')

        else:
            try:
                place = self.search_overloap(place, data)
                self.tab[place] = None                                                  #Przypadek kiedy otrzymany hash to None
                self.tab[place] = None                              #Czyli mogla byc kolizja a element pierwotny z tym hashem zostal usuniety

            except NotFoundError:
                print('Zadany element nie występuje')


    def __str__(self):
        x = '{'
        for k,v in enumerate(self.tab):
            if v is None:
                x += f'None,'
            else:

                x += f' {v.key} : {v.value},'
        x += ' }'
        return x


class Element:
    def __init__(self,key,value):
        self.key = key
        self.value = value


def test1(c1 = 1, c2 = 0):
    hash = Hashtable(13,c1=c1,c2=c2)
    for i in range(1, 16):
        if i == 6:
            hash.insert(Element(18, chr(64 + i)))
        elif i == 7:
            hash.insert(Element(31, chr(64 + i)))
        else:
            hash.insert(Element(i, chr(64 + i)))
    print(hash)
    print(hash.search(5))
    print(hash.search(14))
    hash.insert(Element(5, "Z"))

    print(hash.search(5))
    hash.remove(5)
    print(hash)
    print(hash.search(31))
    hash.insert(Element('test','W'))
    print(hash,'\n\n')



def test2(c1 = 1, c2 = 0):
    hash = Hashtable(13,c1=c1,c2=c2)
    for i in range(1,14):
        hash.insert(Element(i*13,chr(64+i)))

    print(hash,'\n\n')







def main():
    test1()
    test2()
    # Z próbkowaniem liniowym wzystkie miejsca w tablicy zostały zajęte
    test2(c1=0,c2=1)
    # Z próbkowaniem kwadratowym funkcja nie była w stanie wstawić wszystkich elementow, dlatego ze wielokrotnosci 13 za kazdym razem
    #otrzymaly z funkcji haszujacej wartosc 0, a radzenie sobie z kolizja dla probkowania kwadratowego nie osiaga wszsytkich indeksow listy
    #tylko zaczyna je od pewnego momentu powtarzac. Dlatego w funkcji do radzenia sobie z kolizja dodałem warunek ktory ogranicza ilosc wywolan
    #bez niego program wpadł by w nieskończoną pętle.
    print('\n\n\n')
    test1(c1=0,c2=1)


if __name__ == '__main__':
    main()
