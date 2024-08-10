class Father_Cls:
    __base: int

    def __init__(self, base) -> None:
        self.__base = base

    def add(self, num):
        return self.__base + num


class Father2_Cls:
    __base: int
    __b: int

    def __init__(self, base) -> None:
        self.__base = base

    def minus(self, num):
        return self.__base - num


class Son_Cls(Father_Cls, Father2_Cls):
    __base: int

    def __init__(self, base_a, base_b):
        Father_Cls.__init__(self, base_a)
        Father2_Cls.__init__(self, base_a)

        self.__base = base_b

    def add(self):
        return Father_Cls.add(self, self.__base)

    def minus(self):
        return Father2_Cls.minus(self, self.__base)

    def multiplied(self, c):
        return self.__base * c


father = Father_Cls(10)
print('father call add :', father.add(20))

father2 = Father2_Cls(10)
print('father2 call minus :', father2.minus(20))

son = Son_Cls(10, 20)

print('son call add:', son.add())
print('son call minus:', son.minus())
print('son call multiplied:', son.multiplied(10))
