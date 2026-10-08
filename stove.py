from cooking import CookingPlan


class StovePlan(CookingPlan):
    def __init__(self, dishName):
        super().__init__(dishName)

    def cook(self):
        instructions = ["Prepare the stovetop and pan.", "Place " + self.dishName + " in the pan.", "Cook using the recipe's stovetop instructions."]
        return instructions