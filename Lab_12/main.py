#5/5
import time

def naive_method(path,pattern):
    with open(path, encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    #Indeks w tekscie
    m = 0
    start_idx = 0
    #Indeks we wzorcu
    i = 0
    counter = 0
    compare = 0
    find_idx = []
    if len(pattern) == 0:
        return 0

    while start_idx < len(S):

        compare += 1

        '''Jeżeli indeks aktualnego elementu wzorca jest rowny dlugosci -
        znalezlismy wzorzec
        '''

        if i == len(pattern):
            '''aktualizacja zmiennych'''
            find_idx.append(m - len(pattern))
            counter += 1
            i = 0
            start_idx += 1
            m = start_idx
            continue

        '''Jeżeli znaleźliśmy niezgodność'''

        if S[m] != pattern[i]:

            #Przsuniecie poczatku wyszukania o jeden znak
            start_idx += 1
            #Aktualizacja indeksu aktualnie przegladanego
            m = start_idx
            #Ustawienie aktualnego indeksu patternu na 0
            i = 0
            continue

        #Jeżeli znaki się zgadzaja - inkrementujemy

        m += 1
        i += 1

    return counter,compare,find_idx



def hash(word,d=256,q=101):
    hw = 0
    N = len(word)
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q

    return hw


def RabinKarp(path,pattern,d=256,q=101):
    with open(path, encoding='utf-8') as f:
        text = f.readlines()


    counter = 0
    compare = 0
    coll = 0
    S = ' '.join(text).lower()
    M = len(S)
    N = len(pattern)

    hW = hash(pattern)
    hS = hash(S[0:0 + N])
    m = 0
    h = 1
    for i in range(len(pattern) - 1):
        h = (h * d) % q

    while m < M - N + 1:


        compare += 1

        if hS == hW:

            if S[m:m+N] == pattern:
                counter += 1

            else:
                coll += 1

        if m + N < M :
            hS = (d*(hS - ord(S[m]) * h) + ord(S[m+N])) % q

            if hS < 0:
                hS+=q
        m += 1


    return counter,compare,coll


def kmp_table(pattern):
    T = []

    pos = 1
    cnd = 0
    T.append(-1)

    while pos < len(pattern) :
        if pattern[pos] == pattern[cnd]:
            T.append(T[cnd])
        else:
            T.append(cnd)
            while cnd >= 0 and pattern[pos] != pattern[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1

    T.append(0)
    T[pos] = cnd
    return T






def kpm_search(path,pattern):
    with open(path, encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    m = 0
    i = 0
    T = kmp_table(pattern)
    P = []
    nP = 0
    compare = 0

    while m < len(S):
        compare += 1
        if pattern[i] == S[m]:
            m += 1
            i += 1

            if i == len(pattern):
                P.append(m - i)
                nP += 1
                i = T[i-1]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1

    return len(P),compare








t_start = time.perf_counter()
value = naive_method('lotr.txt','time.')
t_stop = time.perf_counter()
print(f'Wyniki dla metody naiwnej')
print(f'{value[0]} ; {value[1]} ')
# print(f'Czas wykonania: {t_stop - t_start}')

t_start = time.perf_counter()
value = RabinKarp('lotr.txt','time.')
t_stop = time.perf_counter()
print('Wyniki dla Rabina Karpa:')

print(f'{value[0]} ; {value[1]} ; {value[2]}')
# print(f'Czas wykonania: {t_stop - t_start}')



t_start = time.perf_counter()
value = kpm_search('lotr.txt','time.')
t_stop = time.perf_counter()
print('Wyniki dla KMP')
print(f'{value[0]} ; {value[1]} ')
