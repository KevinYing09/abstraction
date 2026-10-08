from cooking import CookingPlan


class OvenPlan(CookingPlan):
    def __init__(self, dishName):
        super().__init__(dishName)

    def cook(self):
        instructions = ["Prepare the oven and baking dish.", "Place " + self.dishName + " in the baking dish.", "Bake using the recipe's oven instructions."]
        return instructions