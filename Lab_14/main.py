#5/5
#skończone
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x} {self.y}'


def turning(pt1: Point, pt2: Point,pt3: Point):
    '''Funkcja wyznaczajaca skrętność punktów'''
    value = (pt2.y - pt1.y)*(pt3.x - pt2.x) - (pt3.y - pt2.y)*(pt2.x - pt1.x)
    #prawoskrętne
    if value > 0:
        return 0
    #lewoskrętne
    elif value < 0:
        return 1
    #współliniowe
    else:
        return 2


def is_between(p: Point, q: Point, r: Point):
    '''Funkcja sprawdzająca czy punkt q jest pomiędzy p i r'''

    if ((r.x <= q.x <= p.x) or ( p.x <= q.x <= r.x)) and ((r.y <= q.y <= p.y) or ( p.y <= q.y <= r.y)):
        return True

    return False


def jarvis_algorithm(lst,is_second_version = False):
    init_idx = 0
    #Znajdowanie skrajnie lewego indeksu (z waurnkiem na wybór dolnego w razie potrzeby)
    for i in range(len(lst)):
        if lst[init_idx].x > lst[i].x:
            init_idx = i
        elif lst[init_idx].x == lst[i].x:
            if lst[init_idx].y > lst[i].y:
                init_idx = i

    #zmienne pomocnicze
    p = init_idx
    score_lst = []

    #pętla główna programu
    while True:
        score_lst.append(lst[p])
        q = p + 1
        if q == len(lst):
            q = 0


        for r in range(len(lst)):
            if turning(lst[p],lst[q],lst[r]) == 0:
                q = r

            if is_second_version:
                if turning(lst[p],lst[r],lst[q]) == 2 and is_between(lst[p], lst[q], lst[r]):
                    q = r

        p = q

        if p == init_idx:
            break

    return score_lst



def main():
    lst = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    lst_of_point = [Point(elem[0], elem[1]) for elem in lst]
    x = jarvis_algorithm(lst_of_point)
    y = jarvis_algorithm(lst_of_point,is_second_version=True)
    print(x)
    print(y)

if __name__ == '__main__':
    main()