from calorie_req import *
from imports import *
from recipes import *

OPENROUTER_API_KEY = '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'

recipe_dataset = pd.read_csv('batch1.csv')


def get_model_response(target, meal_time = None, past_conditions = None, ingredients = None):
    if ingredients is None:
        return recipes_from_dataset(target, meal_time, past_conditions)
    
    if meal_time is not None:
        prompt = f'''
            You are an expert nutritionist and chef.
            From the provided ingredients : {ingredients}
            Provide a healthy recipe for {meal_time}.       
            '''
    else:
        prompt = f'''
            You are an expert nutritionist and chef.
            From the provided ingredients : {ingredients}
            Provide one healthy recipe each for breakfast, lunch and dinner.       
            '''
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
    })
    )
    return response.text


print(get_model_response())
# st.title("Making India Fit")

# if 'history' not in st.session_state:
#     st.session_state['history'] = []

# user_message = st.text_input("Your Message", key="input")

# if st.session_state.input:
#     st.session_state.history.append("You: " + user_message)

#     response = get_model_response(user_message)

#     st.session_state.history.append("Mixtral: " + response)

#     st.session_state.input = ""

# for message in st.session_state.history:
#     st.text(message)
