# 5/5
class Root:
    def __init__(self):
        self.root = None

    def insert(self,node):
        self.root = insert(self.root,node)

    def search(self,key):
        help = self.root
        return search(help,key)

    def delete(self,key):
        self.root = delete_node(self.root,key)

    def height(self):
        return height(self.root)


    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node != None:
            self._print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.data,end="\n\n")

            self._print_tree(node.left, lvl + 5)

    def print(self):
        lst = []
        def collect_all(root):
            if root is None:
                return None

            collect_all(root.left)
            lst.append(root)
            collect_all(root.right)


        collect_all(self.root)
        lst.sort(key = lambda x : x.key)
        return lst


class Node:
    def __init__(self,key,data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.key} : {self.data}'

    def __repr__(self):
        return self.__str__()


def insert(root,node):
    if root is not None:
        if root.key > node.key:
            root.left = insert(root.left, node)       #Jezeli klucz wiekszy, wybierz prawa sciezke

        elif root.key < node.key:
            root.right = insert(root.right, node)             #Jezeli klucz mniejszy, wybierz lewa sciezke

        else:
            root.data = node.data           # Nadpisanie elementu
            return root

    else:
        return node

    return root

def search(root,key):

    if root.key > key:
        root = search(root.left, key)       #Jezeli klucz mniejszy, wybierz lewa sciezke


    elif root.key < key:
        root = search(root.right, key)          #Jezeli wiekszy, wybierz prawa sciezke


    else :
        return root.data                        #Gdy sa rowne zwroc


    return root


def delete_node(root, key):


    if root.key > key:
        root.left = delete_node(root.left, key)              #Jezeli klucz mniejszy, wybierz lewa sciezke


    elif root.key < key:
        root.right = delete_node(root.right, key)            #Jezeli wiekszy, wybierz prawa sciezke


    else:
                                                #Element do usuniecia znaleziony
        if root.right is None:
            help_node = root.left
            root = None
            return help_node
                                                                #Przypadek gdy jest jedno dziecko lub nie ma

        elif root.left is None:
            help_node = root.right
            root = None
            return help_node

        else:


            help_node = root
            help_node = help_node.right
            while help_node.left is not None:  # Wyszukiawnei minimalnego elementu prawego półdrzewa
                help_node = help_node.left

            root.data = help_node.data
            root.key = help_node.key  # Wrzucenie minimalnego elementu w miejsce usuwanego elementu

            root.right = delete_node(root.right, help_node.key)  #Podmiana prawego podrzewa





    return root

def height(root):
    if root is None:
        return -1

    left_side = height(root.left)
    right_side = height(root.right)

    if right_side > left_side:
        return right_side +1


    else:
        return left_side + 1



def main():
    a = Root()
    a.insert(Node(50,'A'))
    a.insert(Node(15,'B'))
    a.insert(Node(62,'C'))
    a.insert(Node(5,'D'))
    a.insert(Node(20,'E'))
    a.insert(Node(58,'F'))
    a.insert(Node(91,'G'))
    a.insert(Node(3,'H'))
    a.insert(Node(8,'I'))
    a.insert(Node(37,'J'))
    a.insert(Node(60,'K'))
    a.insert(Node(24,'L'))
    a.print_tree()
    print(a.print())
    print(a.search(24))
    a.insert(Node(20,'AA'))
    a.insert(Node(6,"M"))
    a.delete(62)
    a.insert(Node(59,"N"))
    a.insert(Node(100,'P'))
    a.delete(8)
    a.delete(15)
    a.insert(Node(55,"R"))
    a.delete(50)
    a.delete(5)
    a.delete(24)
    print(a.height())
    print(a.print())
    a.print_tree()


if __name__ == '__main__':
    main()


