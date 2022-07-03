#1.5/2 --- Czas oddania
#Skończone
import time
import numpy as np
from collections import defaultdict



def hash(word,d=256,q=101):
    hw = 0
    N = len(word)
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q

    return hw



def RabinKarpSet(path,pattern_strings,d=256,q=101,P = 0.001,b_const = 1):
    with open(path, encoding='utf-8') as f:
        text = f.readlines()


    S = ' '.join(text).lower()
    M = len(S)
    n = len(pattern_strings)
    #Tutaj zakladamy, ze wszystkie napisy sa tej samej dlugosci
    N = len(pattern_strings[0])
    b = -n * np.log(P/(np.log(2)**2))
    k = b/(n*np.log(2))

    b = int(np.round(b))
    #Potencjalne zwiększenie rozmiaru tablicy
    b = b * b_const
    k = int(np.round(k))
    hsubs = set()
    bloom_tab = [0 for i in range(b)]


    #Tablica liczb pierwszych o długosci k stworzona na 'sztywno'(dla obu przypadków k = 9)
    prime_numbers = [103, 107, 109, 113, 127, 131, 137, 139,151]
    for sub in pattern_strings:
        hsubs.add(hash(sub))
        for elem in prime_numbers:
            bloom_tab[hash(sub,q=elem) % b] = 1

    h = 1
    for i in range(N- 1):
        h = (h * d) % q

    hS = hash(S[0:0 + N])
    m = 0
    occur_elem = defaultdict(list)
    false_positive = 0
    while m < M - N + 1:

        if hS in hsubs :

            flag = True

            for elem in prime_numbers:
                if bloom_tab[hash(S[m:m+N],q=elem) % b] == 0:
                    flag = False
            if flag:
                if S[m:m + N] in pattern_strings:
                    occur_elem[S[m:m+N]].append(m)
                else:
                    false_positive += 1



        #Rolling hash
        if m + N < M :
            hS = (d*(hS - ord(S[m]) * h) + ord(S[m+N])) % q

            if hS < 0:
                hS+=q

        m += 1

    return dict(occur_elem),false_positive


def main():

    #Dane wejściowe
    strings = ['costamc','pythonpl','gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']
    lst = ['gandalf']


    t_start1 = time.perf_counter()
    value,false_positive = RabinKarpSet('lotr.txt',strings)
    t_stop1 =  time.perf_counter()

    t_start2 = time.perf_counter()
    value2,false_positive2 = RabinKarpSet('lotr.txt',lst)
    t_stop2 =  time.perf_counter()



    print('Wynik zawiera słownik gdzie kluczami są poszczególne wyrazy a wartościami listy z indeksami wystąpienia danego elementu',end='\n\n')

    print(f'Lista kluczy: {value.keys()}')
    print(f'Jak możemy zaobserwować na powyższej liscie nie ma elementu "{strings[0]}" oraz "{strings[1]}" co znaczy, że filtr prawidłowo stwierdził,że\n'
          f'te elementy nie występują w tekscie',end='\n\n')
    print(f'Wynik: {value}',end='\n\n')

    print(f'Czas działania dla 1 wzorca: {t_stop2 - t_start2}')
    print(f'Czas działania dla 22 wzorców: {t_stop1 - t_start1}')
    print('Jak widzimy czas nie wzrósł 22-krotnie a maksymalnie 5-krotnie (tutaj powinna byc analiza dla wielu wywolan funkcji, lecz niestety\n'
          'zabraklo mi czasu na dodanie tego elementu).',end='\n\n')

    print(f'Fałszywie pozytywne detekcję dla 1 wzorca: {false_positive2}')
    print(f'Fałszywie pozytywne detekcję dla 22 wzorców: {false_positive}')


    value, false_positive = RabinKarpSet('lotr.txt', lst,b_const=2)
    print(f'Fałszywie pozytywne detekcję dla 1 wzorca po dwukrotnym zwiększeniu rozmiaru tablicy: {false_positive}')

    value, false_positive = RabinKarpSet('lotr.txt', strings, b_const=2)
    print(f'Fałszywie pozytywne detekcję dla 22 wzorców po dwukrotnym zwiększeniu rozmiaru tablicy: {false_positive}')




#
# if __name__ == '__main__':
#     main()

y = 'stuff;thing;junk;'
z = y.split(';')
print(z)