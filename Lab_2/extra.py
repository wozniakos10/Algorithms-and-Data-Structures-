# 2/2
class Element:
    def __init__(self, data):
        self.data = data
        self.next = None


def nill():
    return None


def create():
    return nill()


def cons(el,list):
    a = Element(el)
    if list is None:
        return a
    a.next = list
    return a


def first(list):
    return list.data


def rest(list):
    return list.next


def is_empty(list):
    if list is None:
        return True


def add_end(el, lst):
    if is_empty(lst):
        return cons(el, lst)  # dojście do końca i wstawienie tam elementu
    else:
        first_el   = first(lst)       # podział listy na: pierwszy element
        rest_lst  = rest(lst)      # i całą resztę
        recreated_lst = add_end(el, rest_lst) # 'zejście 'w dół' rekurencji z przekazaniem dodawanego elementu, przy powrocie 'w górę' zwracana jest odtworzona lista
        return cons(first_el, recreated_lst)   # cons dołącza pierwszy element do 'odtwarzanej' przez rekurencję listy
                                                                  # zmienne first-el, rest_lst i recreated_lst są wprowadzone pomocniczo, dla wyjaśnienia działania funkcji

def remove_last(lst):
    if length(lst) <= 1:
        lst = None

    else:
        first_el = first(lst)
        rest_lst = rest(lst)
        recreated_lst = remove_last(rest_lst)
        return cons(first_el, recreated_lst)


def destroy(list):
    list = None


def add(el,list):
    return cons(el,list)


def remove(list):
    return rest(list)


def get(list):
    return first(list)


def length(list):
    counter = 0
    while list:
        list = rest(list)
        counter += 1
    return counter


def take(size,list):
    x = create()
    if size > length(list):
        return list

    while size > 0:
        x = add_end(first(list),x)
        size -= 1
        list = rest(list)
    return x


def drop(size,list):
    if size >= length(list):
        return create()
    while size > 0:
        list = rest(list)
        size -= 1
    return list

def str(list):
    s = f''
    if list is None:
        return f'[]'

    while list:
        s +=  " " + f'{first(list)}'
        list = rest(list)
    return s



def main():
    llist = create()
    data = [('AGH', 'Kraków', 1919),
            ('UJ', 'Kraków', 1364),
            ('PW', 'Warszawa', 1915),
            ('UW', 'Warszawa', 1915),
            ('UP', 'Poznań', 1919),
            ('PG', 'Gdańsk', 1945)]

    for k, v in enumerate(data):
        llist = add_end(v,llist)
    print(str(llist), '\n')
    print(f'Pierwszy element listy to: {get(llist)}\n')

    llist = remove_last(llist)
    llist = add(data[-1],llist)

    print(f'Lista po usunięciu ostatniego elementu i wstawieniu na początek:\n{str(llist)}\n')

    llist = remove(llist)
    llist = add_end(data[-1],llist)

    print(f'Lista po usunięciu pierwszego elementu i wstawieniu go na koniec:\n{str(llist)}\n')

    print(f'Ilość elementów w liście: {length(llist)}\n')

    take_list = take(3,llist)
    take2_list = take(7,llist)
    drop_list = drop(4,llist)
    drop2_list = drop(7,llist)
    print(f'Nowa lista powstała z 3 pierwszych elementów:\n{str(take_list)}\n')

    print(f'Nowa lista powstała z pominięciem pierwszych 4 elementów:\n{str(drop_list)}\n')

    print(f'Nowa lista powstała z 7 pierwszych elementów(czyli ma przypisać całą listę):\n{str(take2_list)}\n')

    print(f'Nowa lista powstała z pominięciem pierwszych 7 elementów(czyli zwróci pustą listę):\n{str(drop2_list)}\n')

    llist = destroy(llist)

    print(f'Długość listy po usunięciu: {length(llist)}')

    print(f'Czy lista jest pusta? {is_empty(llist)}')


if __name__ == '__main__':
    main()








