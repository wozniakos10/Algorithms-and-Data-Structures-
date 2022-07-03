# 5/5
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



def matrix_inverse(matrix):
    result = Matrix((matrix.size()[1],matrix.size()[0]))
    for i in range (matrix.size()[0]):
        for k in range(matrix.size()[1]):
            result[k,i] = matrix[i,k]
    return result



def main():
    x = Matrix([[1,0,2],[-1,3,1]])

    transp = matrix_inverse(x)
    print(f'Transponowanie:\n\n{transp}\n\n')

    z = Matrix((2,3),1)
    sum = z + x
    print(f'Dodawanie:\n\n{sum}\n\n')

    y = Matrix([[3,1],[2,1],[1,0],[1,0]])

    mult = x*y
    print(f'Mnożenie\n\n{mult}')

if __name__ == "__main__":
    main()

