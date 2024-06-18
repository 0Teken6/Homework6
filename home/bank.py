class Bank:
    def __init__(self,name,age,money,key):
        self._name=name
        self._age=age
        self.__money=money
        self.__key=key

    def set_name(self,name):...

    def get_name(self):...

class Bank2(Bank):
    def __init__(self, name, age, money, key):
        super().__init__(name, age, money, key)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class Bank3(Bank2):
    def __init__(self, name, age, money, key):
        super().__init__(name, age, money, key)

    @property
    def age_prop(self):
        return self._age

    @age_prop.setter
    def age_prop(self, age):
        self._age = age

    @property
    def money_prop(self):
        return self.__money

    @money_prop.setter
    def money_prop(self, money):
        self.__money = money

    @property
    def key_prop(self):
        return self.__key

    @key_prop.setter
    def key_prop(self, key):
        self.__key = key


