# 2/2
class Matrix:
    def __init__(self,data,base=0):
        self.base = base
        self.data = data
        if isinstance(self.data,tuple):
            self.__matrix = []
            column = []

            for i in range(self.data[0]):
                for j in range(self.data[1]):
                    column.append(self.base)
                self.__matrix.append(column)
                column = []

        else:
            self.__matrix = self.data


    def __getitem__(self, item):
        return self.__matrix[item[0]][item[1]]


    def __setitem__(self, key, value):
        self.__matrix[key[0]][key[1]] = value


    def size(self):
        return len(self.__matrix), len(self.__matrix[0])


    def __add__(self,other):
        if len(self.__matrix) == len(other.__matrix) and len(self.__matrix[0]) == len(other.__matrix[0]):  #Checking sizes
            x = Matrix((len(self.__matrix), len(self.__matrix[0])))
            for i in range(len(self.__matrix)):
                for j in range(len(self.__matrix[0])):                                        #looping through and adding
                    x[i,j] = self.__matrix[i][j] + other.__matrix[i][j]

            return  x


    def __mul__(self, other):
        x = True
        for k,v in enumerate(self.__matrix):
            if len(v) != len(other.__matrix):                                                 #Checking sizes
                x = False
                return x

        if x:
            matrix = Matrix((len(self.__matrix), len(other.__matrix[0])))
            value = 0

            for i in range((len(self.__matrix))):                                                     #If sizes are ok, looping through and multiply
                for j in range(len(other.__matrix[0])):
                    for k in range(len(other.__matrix)):
                         value += self.__matrix[i][k] * other.__matrix[k][j]
                    matrix[i,j] = value
                    value = 0

            return matrix


    def __str__(self):
        x = f''
        for i in self.__matrix:
            x += str(i) + '\n'
        return x


def det(matrix):
    value = 1
    i = 1                                                       #Obsługa przypadku kiedy pierwszy element jest zerowy                                                           ds
    while matrix[0,0] == 0:                                     #Jeśli jest zerowy to zamien go z najblizszym wierszem i zmien znak wyznacznika na przeciwny
                                                                #czyli pomnóż przez -1
        help_value = matrix[0,:]
        matrix[0,:] = matrix[i,:]
        matrix[i, :] = help_value
        value = value *(-1)
        i += 1

    if matrix.size() == (2,2):
        return matrix[0,0] * matrix[1,1] - matrix[0,1] * matrix[1,0]        #Sprawdzenie rozmiaru

    else:
        r = matrix.size()[0]
        c = matrix.size()[1]
        matr = Matrix((r-1,c-1))                            #Macierz pomocniczna o rozmiarze n-1
        for k in range(matr.size()[0]):
            for v in range(matr.size()[0]):
                matr[k,v] = det(Matrix([[matrix[0,0],matrix[0,1+v]],[matrix[1+ k,0],matrix[k+1,v+1]]]))         #Wypelnianie macierzy poszczegolnymi wyznacznikami


        return (1/matrix[0,0])**(matrix.size()[0] - 2) * det(matr) * value          #Zwrocenie wyznacznika pomnozonego przez odpowiedni skalar i uwzględniona zmiana znaku
                                                                                    #(Jeśli wiersze były zamieniane)


def main():
    x = Matrix([[5 , 1 , 1 , 2 , 3],

    [4 , 2 , 1 , 7 , 3],

    [2 , 1 , 2 , 4 , 7],

    [9 , 1 , 0 , 7 , 0],

    [1 , 4 , 7 , 2 , 2]])

    print(x)
    print(det(x))

    z = Matrix([ [0 , 1 , 1 , 2 , 3],
         [4 , 2 , 1 , 7 , 3],
         [2 , 1 , 2 , 4 , 7],
         [9 , 1 , 0 , 7 , 0],
         [1 , 4 , 7 , 2 , 2]])

    print(z)
    print(det(z))


if __name__ == '__main__':
    main()