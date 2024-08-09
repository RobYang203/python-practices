class Ex1Cls:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_all(self):
        print(f'a = {self.a} , b = {self.b}')


ex1 = Ex1Cls(5, 10)

ex1.print_all()

print('ex1 a out call :', ex1.a)


class Ex2Cls:
    def __init__(self, list) -> None:
        self.__list = list

    def print_list(self):
        for i in self.__list:
            print(i)

    @property
    def list(self):
        return self.__list

    @property
    def double_list(self):
        return self.__list * 2

    @list.setter
    def list(self, new_data):
        self.__list = new_data
        print('list changed:', new_data)

    @list.deleter
    def list(self):
        del self.__list
        print('list deleted')


ex2 = Ex2Cls([1, 2, 3, 4, 6])

ex2.print_list()

print(ex2.list)
print(ex2.double_list)

ex2.list = [0, 6, 55, 43, 3]

del ex2.list
