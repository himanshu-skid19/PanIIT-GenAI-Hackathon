from imports import *
from calorie_req import *

recipe_dataset = pd.read_csv("Final_Recipies.csv")

def recipes_from_dataset(target_weight, number_of_days, age, weight, height, gender, pa, is_veg, meal_type = None, diet_type = "Balanced"):
    if meal_type is None:
        s_factor = 1
        done = False
        counter = 0
        breakfast_set = recipe_dataset[(recipe_dataset['meal_time'] == "Breakfast") & (recipe_dataset['Diet Type'] == diet_type) & (recipe_dataset['Veg'] == is_veg)]
        lunch_set = recipe_dataset[(recipe_dataset['meal_time'] == "Lunch") & (recipe_dataset['Diet Type'] == diet_type) & (recipe_dataset['Veg'] == is_veg)]
        dinner_set = recipe_dataset[(recipe_dataset['meal_time'] == "Dinner") & (recipe_dataset['Diet Type'] == diet_type) & (recipe_dataset['Veg'] == is_veg)]
        while(counter < 20):
            counter += 1
            breakfast = breakfast_set.sample(1)
            lunch = lunch_set.sample(1)
            dinner = dinner_set.sample(1)
            s_factor, done = check_meal(breakfast,lunch, dinner, diet_type, target_weight, number_of_days, age, weight, height, gender, pa) 
            if(done):
                return breakfast, lunch, dinner, s_factor
        return breakfast, lunch, dinner, 1
    else:
        meal_set = recipe_dataset[(recipe_dataset['Meal Type'] == meal_type) & (recipe_dataset["Diet Type"] == diet_type)]
        meal = meal_set.sample(1)
        return meal
