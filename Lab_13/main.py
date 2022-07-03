#5/5
import numpy as np

#podpunkt A
def string_compare(P: str, T: str, i: int, j: int ) -> int:
    """
    :param P:
    :param T:
    :param i:
    :param j:
    :return:
    """
    if i == 0:
        return len(T[:j])

    if j == 0:
        return len(P[:i])

    zamian = string_compare(P,T,i-1,j-1) + (P[i]!=T[j])
    wstawien = string_compare(P,T,i,j-1) + 1
    usuniec = string_compare(P,T,i-1,j)  + 1

    min_cost = min(zamian,wstawien,usuniec)

    return  min_cost

#podpunkt B i D
def string_compare_pd(P: str, T: str, i: int, j: int, is_d = False ) -> int:
    """
    :param P:
    :param T:
    :param i:
    :param j:
    :return:
    """
    #stworzenie tablicy i wypelnienie wedle wzoru
    if is_d:
        d = np.zeros((len(P), len(T)), dtype=int)
        for i in range(1, len(d)):
            d[i][0] = i

            # tablica rodzicow
        parent = np.full((len(P), len(T)), 'X')
        for i in range(1, len(parent)):
            parent[i][0] = 'D'

    else:
        d = np.zeros((len(P), len(T)),dtype=int)
        for i in range(len(d)):
            d[0][i] = i
            d[i][0] = i

            #tablica rodzicow
        parent = np.full((len(P) , len(T) ),'X')
        for i in range(1,len(parent)):
            parent[0][i] = 'I'
            parent[i][0] = 'D'


    for i in range(1,d.shape[0]):
        for j in range(1,d.shape[1]):
            zamian = d[i-1][j-1] + (P[i]!=T[j])
            wstawien = d[i][j-1] +1
            usuniec = d[i-1][j] +1

            min_cost = min(zamian, wstawien, usuniec)
            if min_cost == zamian:
                #sprawdzenie czy była zamiana czy nie
                if P[i]!=T[j]:
                    parent[i][j] = 'S'
                else:
                    parent[i][j] = 'M'

            elif min_cost == wstawien:
                parent[i][j] = 'I'

            elif min_cost == usuniec:
                parent[i][j] = 'D'

            d[i][j] = min_cost


    return d,parent


#podpunkt C
def find_path(parrent: np.ndarray):
    elem = parrent[-1][-1]
    i = parrent.shape[0] -1
    j = parrent.shape[1] - 1
    lst = []

    while elem != 'X':
        lst.append(elem)

        if parrent[i][j] == 'M' or parrent[i][j] == 'S':
            i -= 1
            j -= 1

        elif parrent[i][j] == 'I':
            j -= 1

        elif parrent[i][j] == 'D':
            i -= 1

        elem = parrent[i][j]



    lst = lst[::-1]
    s = ''
    s = s.join(lst)
    return s


def goal_cell(P,T,D):
    i = len(P) - 1
    j = 0

    for k in range(1,len(T)):
        if D[i][k] < D[i][j]:
            j = k

    return j


#podpuknt e
def string_compare_pd_e(P: str, T: str, i: int, j: int ) -> int:
    """

    :param P:
    :param T:
    :param i:
    :param j:
    :return:
    """

    #stworzenie tablicy i wypelnienie wedle wzoru
    d = np.zeros((len(P), len(T)),dtype=int)

    for i in range(d.shape[0]):
        d[i][0]= i

    for i in range(d.shape[1]):
        d[0][i] = i

        #tablica rodzicow
    parent = np.full((len(P) , len(T) ),'X')

    for i in range(1,parent.shape[0]):
        parent[i][0] = 'D'

    for i in range(1,parent.shape[1]):
        parent[0][i] = 'I'


    for i in range(1,d.shape[0]):
        for j in range(1,d.shape[1]):
            if P[i]!=T[j]:
                zamian = d[i-1][j-1]  + 1e16
            else:
                zamian = d[i - 1][j - 1]

            wstawien = d[i][j-1] +1
            usuniec = d[i-1][j] +1

            min_cost = min(zamian, wstawien, usuniec)
            if min_cost == zamian:
                #sprawdzenie czy była zamiana czy nie
                if P[i]!=T[j]:
                    parent[i][j] = 'S'
                else:
                    parent[i][j] = 'M'

            elif min_cost == wstawien:
                parent[i][j] = 'I'

            elif min_cost == usuniec:
                parent[i][j] = 'D'

            d[i][j] = min_cost

    return d[-1][-1],parent


def main():

    P2 = ' kot'
    T2 = ' pies'

    P3 = ' biały autobus'
    T3 = ' czarny autokar'

    P4 = ' thou shalt not'
    T4 = ' you should not'

    P5 = 'ban'
    T5 = ' mokeyssbanana'

    P6 = ' democrat'
    T6 = ' republican'

    T7 = ' 243517698'
    P7_lst = [2,4,3,5,1,7,6,9,8]
    P7_lst.sort()
    P7 = ' '
    P7_label = ''.join(map(str,P7_lst))
    P7 += P7_label


    print('Podpunkt a - przykład z kotem i psem:')
    val = string_compare(P2,T2,len(P2) -1,len(T2) -1)
    print(val,end='\n\n')


    print('Podpunkt b - przykład z autobusami:')
    val,parent = string_compare_pd(P3,T3,len(P3) -1,len(T3) -1)
    print(val[-1][-1],end='\n\n')


    val,parent = string_compare_pd(P4,T4,len(P4) -1,len(T4) -1)
    print('Podpunkt c - napis reprezentujący ścieżkę')
    label = find_path(parent)
    print(label,end='\n\n')


    print('Podpunkt d - ')
    val,parent = string_compare_pd(P5,T5,len(P5) -1,len(T5) -1,is_d=True)
    idx = goal_cell(P5,T5,val)
    print(idx - (len(P5) - 1),end='\n\n')


    val,parent = string_compare_pd_e(P6,T6,len(P6) - 1, len(T6) - 1)
    path = find_path(parent)
    lst = [elem for elem in path if elem != 'D']
    help_lst = []
    for i in range(len(lst)):
        if lst[i] == 'M':
            help_lst.append(i)
    label = ''.join([T6[elem + 1] for elem in help_lst])
    print('Podpunkt e - najdłuższa wspólna sekwencja')
    print(label,end='\n\n')


    val,parent = string_compare_pd_e(P7,T7,len(P7) - 1, len(T7) - 1)
    path = find_path(parent)
    lst = [elem for elem in path if elem != 'D']
    help_lst = []
    for i in range(len(lst)):
        if lst[i] == 'M':
            help_lst.append(i)
    label = ''.join([T7[elem + 1] for elem in help_lst])
    print('Podpunkt f - najdłuższa podsekwencja monotoniczna')
    print(label,end='\n\n')

if __name__ == '__main__':
    main()


