from abc import ABC, abstractmethod


class CookingPlan(ABC):
    def __init__(self, dishName):
        self.dishName = dishName

    def getDishName(self):
        return self.dishName

    @abstractmethod
    def cook(self):
        pass