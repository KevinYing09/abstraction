from cooking import CookingPlan
from oven import OvenPlan
from stove import StovePlan
from camping import CampingPlan

def showPlan(plan):
    print(plan.getDishName())
    instructions = plan.cook()
    for instruction in instructions:
        print(instruction)

def main():
    plan = OvenPlan("Cake")
    showPlan(plan)

main()