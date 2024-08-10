import abc


class Person(abc.ABC):
    @abc.abstractmethod
    def define_sex(self):
        raise NotImplemented


class Girl(Person):
    def define_sex(self):
        print('I am a girl')
        
class Boy(Person):
    def define_sex(self):
        print('I am a boy')

luna = Girl()

luna.define_sex()

tony = Boy()

tony.define_sex()