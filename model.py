from imports import *
from recipes import *
from calorie_req import *

OPENROUTER_API_KEY = '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'

recipe_dataset = pd.read_csv('batch1.csv')

recipe_dataset = pd.read_csv('Final_Recipies.csv')

def http_request(prompt):
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    },
    data=json.dumps({
        "model": "mistralai/mixtral-8x7b-instruct", # Optional
        "messages": [
        {"role": "user", "content": prompt}
        ]
    }))
    print(response.text)
    return response.text


def get_model_response(target_weight, number_of_days, age, weight, height, gender, pa, is_veg, meal_type = None, diet_type = "Balanced", ingredients = None):
    if ingredients is None:
        responses = []
        try:
            breakfast, lunch, dinner, scale_factor = recipes_from_dataset(target_weight, number_of_days, age, weight, height, gender, pa, is_veg, meal_type, diet_type)
            for i in [breakfast, lunch, dinner]:
                i[['Calories','Protein', 'Fat', 'Sugars', 'Carbohydrates']] = i[['Calories','Protein', 'Fat', 'Sugars', 'Carbohydrates']]*scale_factor
                prompt = f"""
                        You are an expert nutritionist and chef.
                        For the following meal:
                        Meal: {i.iloc[0]}
                        The description of the meal should include the meal name, the time of the day (breakfast, lunch or dinner), the calories and other nutrients of the meal and the ingredients required to make that meal. 
                        Give your output in a json format.  
                        the json output should be structured as follows
                        '''
                           {
                               "Meal" : "Meal_name",
                               "Desciption" : "Description about the meal",
                               "Calories" : "Total calories in the meal",
                               "Protein" : "Total protein in the meal",
                               "Fat" : "Total fats in the meal",
                               "Carbohydrates" : "Total carbohydrates in the meal",
                               "Sugars" : "Total sugars in the meal",
                               "Ingredients" : "Dictionary containing the ingredients and other info"
                           } 
                        '''
                        """
                response = http_request(prompt)
                response = json.loads(response)
                response = response["choices"][0]["message"]["content"]
                responses.append(response)
        except:
            if is_veg == 0:
                diet = "non-veg"
            else:
                diet = "veg"
            for i in ("breakfast", "lunch", "dinner"):
                prompt = f'''\
                    You are an expert nutritionist and chef.
                    Make one healthy, {diet_type}, {diet} meal for {i}.
                    Also provide the "Calories", "Fat", "Sugars", "Carbohydrates", "Protein" in the meal.
                    Give your output in a json format.       
                    '''
                response = http_request(prompt)
                response = json.loads(response)
                print(response)
                response = response["choices"][0]["message"]["content"]
                responses.append(response)
        return responses                    
                    
    else:
        if meal_type is not None:
            prompt = f'''
                You are an expert nutritionist and chef.
                You are provided with the following set of ingredients : {ingredients}
                Use the provided ingredients to make one healthy, {diet_type} meal for {meal_type}.
                Also provide the "Calories", "Fat", "Sugars", "Carbohydrates", "Protein" in the meal.   
                Give your output in a json format.        
                '''
            response = http_request(prompt)
            response = json.loads(response)
            response = response["choices"][0]["message"]["content"]
            return response
        else:
            responses = []
            for i in ("breakfast", "lunch", "dinner"):
                prompt = f'''\
                    You are an expert nutritionist and chef.
                    You are provided with the following set of ingredients : {ingredients}
                    Use the provided ingredients to make one healthy, {diet_type} meal for {i}.
                    Also provide the "Calories", "Fat", "Sugars", "Carbohydrates", "Protein" in the meal.
                    Give your output in a json format.       
                    '''
                response = http_request(prompt)
                response = json.loads(response)
                response = response["choices"][0]["message"]["content"]
                responses.append(response)
            return responses
