from imports import *
from calorie_req import *

recipe_dataset = pd.read_csv('batch1.csv')

def recipes_from_dataset(target, meal_time = None, diet_type = "balanced", past_conditions = None):
    if past_conditions is not None:
        df = recipe_dataset[(recipe_dataset["target"] == target) and (recipe_dataset["condition"] == past_conditions) and (recipe_dataset["diet_type"] == diet_type)]
    else:
        df = recipe_dataset[(recipe_dataset["target"] == target) and (recipe_dataset["diet_type"] ==diet_type)]
    if meal_time is None:
        breakfast_set = df[df['meal_time'] == "breakfast"]
        flag_b = False
        while flag_b == False:
            breakfast = breakfast_set.sample(1)
            if total_energy_req(breakfast):
                flag_b = True

        
        lunch_set = df[df['meal_time'] == "lunch"]
        flag_l = False
        while flag_l == False:
            lunch = lunch_set.sample(1)
            if total_energy_req(lunch):
                flag_l = True
         
        
        dinner_set = df[df['meal_time'] == "dinner"]
        while flag_l == False:
            dinner = dinner_set.sample(1)
            if total_energy_req(lunch):
                flag_l = True
         
        return breakfast, lunch, dinner
    else:
        meal_set = df[df['meal_time'] == meal_time]
        meal = meal_set.sample(1)
        return meal
