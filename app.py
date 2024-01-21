from calorie_req import *
from imports import *
from recipes import *

OPENROUTER_API_KEY = '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'

recipe_dataset = pd.read_csv('batch1.csv')


# def get_model_response(target, meal_time = None, past_conditions = None, ingredients = None):
#     if ingredients is None:
#         return recipes_from_dataset(target, meal_time, past_conditions)
    
#     if meal_time is not None:
#         prompt = f'''
#             You are an expert nutritionist and chef.
#             From the provided ingredients : {ingredients}
#             Provide a healthy recipe for {meal_time}.       
#             '''
#     else:
#         prompt = f'''
#             You are an expert nutritionist and chef.
#             From the provided ingredients : {ingredients}
#             Provide one healthy recipe each for breakfast, lunch and dinner.       
#             '''
#     response = requests.post(
#     url="https://openrouter.ai/api/v1/chat/completions",
#     headers={
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#     },
#     data=json.dumps({
#         "model": "mistralai/mixtral-8x7b-instruct", # Optional
#         "messages": [
#         {"role": "user", "content": prompt}
#         ]
#     })
#     )
#     return response.text


# print(get_model_response())
# Initialize session states for dynamic content
main_but_css = '''
    <style>
        .big-button {
            height: 3em;
            width: 10em;
            font-size: 1em;
            font-weight: bold;
        }
    </style>

'''

st.markdown(main_but_css, unsafe_allow_html=True)

# Backend functions to generate content
def get_random_content():
    # This function simulates getting content from the backend.
    # Replace this with actual backend logic (e.g., database query, API call).
    phrases = ["Hello, World!", "Streamlit is Awesome!", "Dynamic Content Here!"]
    return random.choice(phrases)

# Initialize session states for content if not already present
for box_num in range(1, 4):
    if f'content_box{box_num}' not in st.session_state:
        st.session_state[f'content_box{box_num}'] = 'Click "Update Content" to generate content.'

# Function to update content in the boxes from the backend
def update_content_from_backend():
    for box_num in range(1, 4):
        st.session_state[f'content_box{box_num}'] = get_random_content()

# Layout of the sidebar
with st.sidebar:
    st.title("Control Panel")

    # Navigation or Section Heading
    st.subheader("Navigation")
    
    # Interactive Widgets
    st.radio("Choose a section", ["Home", "Profile", "Meal History"], index=0)


    # Action Buttons
    if st.button("Logout"):
        st.sidebar.write("Button clicked!")

    # # Use expander for advanced options to keep the sidebar clean
    # with st.expander("Advanced Settings"):
    #     st.checkbox("Enable Advanced Mode")
    #     # More advanced widgets can be placed here

# Layout of the main page
st.title("Welcome!")

# Content boxes in the main area
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("BreakFast")
    st.write(st.session_state['content_box1'])
    st.button("View Ingredients", key='breakfast')

    
with col2:
    st.subheader("Lunch")
    st.write(st.session_state['content_box2'])
    st.button("View Ingredients", key = 'lunch')
    

with col3:
    st.subheader("Dinner")
    st.write(st.session_state['content_box3'])
    st.button("View Ingredients", key = 'dinner')

st.markdown('<button class="big-button">EAT NOW</button>', unsafe_allow_html=True) 

# st.markdown"EAT NOW", key = "eat_now", **{'class': 'big-button'})
# st.button("REPLAN", key = 'replan', **{'class' : 'big-button'})
