from cooking import CookingPlan


class CampingPlan(CookingPlan):
    def __init__(self, dishName):
        super().__init__(dishName)

    def cook(self):
        instructions = ["Prepare the portable stove and camping pot.", "Place " + self.DishName + " in the camping pot.", "Cook using the recipe's portable-stove instructions."]
        return instructions