from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def SummClothes(self):
        pass

    # @property
    # def SummClothes(self):
    #    return f'Все затрачено ткани: {self.param / 6.5 +0.5} + {self.param * 2 +0.3}'


class Costume(Clothes):

    @property
    def SummClothes(self):
        return f'Всего ткани затрачено на костюм: {round(float(self.param) / 6.5 + 0.5, 2)}'


class Coat(Clothes):

    @property
    def SummClothes(self):
        return f'Всего ткани затрачено на пальто: {round(float(self.param) * 2 +0.3, 2)}'

coat = Coat(400)
costume = Costume(55)
print(coat.SummClothes)
print(costume.SummClothes)
print(f'Все затрачено ткани: {costume.SummClothes} + {coat.SummClothes}')
