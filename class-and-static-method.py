class Ex_Cls:
    a = 10

    def __init__(self, a) -> None:
        self.__a = a

    def add(self, b: int):
        return self.__a + b

    @classmethod
    def class_add(cls, b):
        return cls.a + b

    @staticmethod
    def static_add(a, b):
        return a + b


ex1 = Ex_Cls(20)

print('call add:', ex1.add(200))
print('call class add:', Ex_Cls.class_add(200))
print('call static add:', Ex_Cls.static_add(50, 200))
