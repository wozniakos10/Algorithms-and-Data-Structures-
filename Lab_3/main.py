# 5/5
#Skończone
class Queue:
    def __init__(self):
        self.tab = [None for i in range(5)]
        self.size = len(self.tab)
        self.save_idx = 0
        self.read_idx = 0

    def is_empty(self):
        if self.save_idx == self.read_idx:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.tab[self.read_idx]

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.tab[self.read_idx]
        self.read_idx += 1
        if self.read_idx == self.size:
            self.tab[self.read_idx - 1] = None          #obsługa zapętlenia kolejki
            self.read_idx = 0
            return value

        self.tab[self.read_idx - 1] = None
        return value

    def enqueue(self, data):
        self.tab[self.save_idx] = data
        self.save_idx += 1

        if self.save_idx == self.read_idx:
            help_tab = self.tab
            self.tab = realloc(self.tab, self.size * 2)

            self.tab[self.save_idx + 5:] = help_tab[self.save_idx:]        #Rozsuwanie elementów kolejki
            self.size = len(self.tab)
            for i in range(self.save_idx + 1, self.save_idx + 5):       #Wstawienie None pomiedzy read i save
                self.tab[i] = None

            self.read_idx = self.read_idx + 5               #Przestawienie odczytu kolejki na nowe miejsce

        elif self.save_idx == self.size:
            if self.tab[0] is None:
                self.save_idx = 0               #Uwzględnienie zapętlenia na końcu tablicy
                self.tab[self.save_idx] = data

            else:
                self.tab = realloc(self.tab, self.size * 2)
                self.size = len(self.tab)
                self.tab[self.save_idx] = data

    def __str__(self):
        if self.read_idx > self.save_idx:
            '''Sprawdzanie jak wypisywac kolejke'''
            return f'Tablica : {self.tab}\nKolejka: {self.tab[self.read_idx:] + self.tab[:self.save_idx]}\n'            #
        return f'Tablica: {self.tab}\nKolejka: {[self.tab[i] for i in range(self.read_idx, self.save_idx)]}\n'


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i < oldSize else None for i in range(size)]




def main():
    x = Queue()
    for i in range(1, 5):
        x.enqueue(i)

    print(x.dequeue())

    print(x.peek())
    print(x)
    for i in range(5, 9):
        x.enqueue(i)
    print(x)


    while not x.is_empty():
        print(x.dequeue())

    print(x)


if __name__ == '__main__':
    main()

