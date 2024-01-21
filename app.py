from calorie_req import *
from imports import *
from recipes import *
from helper import *

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
            .btn-bd-primary {
    --bs-btn-font-weight: 600;
    --bs-btn-color: var(--bs-white);
    --bs-btn-bg: var(--bd-violet-bg);
    --bs-btn-border-color: var(--bd-violet-bg);
    --bs-btn-hover-color: var(--bs-white);
    --bs-btn-hover-bg: #{shade-color($bd-violet, 10%)};
    --bs-btn-hover-border-color: #{shade-color($bd-violet, 10%)};
    --bs-btn-focus-shadow-rgb: var(--bd-violet-rgb);
    --bs-btn-active-color: var(--bs-btn-hover-color);
    --bs-btn-active-bg: #{shade-color($bd-violet, 20%)};
    --bs-btn-active-border-color: #{shade-color($bd-violet, 20%)};
}
        }
    </style>

'''

bootstrap_css = """
<link rel="stylesheet" href = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
"""

st.markdown(bootstrap_css, unsafe_allow_html=True)
st.markdown(main_but_css, unsafe_allow_html=True)




# Layout of the sidebar
with st.sidebar:
    st.title("Control Panel")

    # Navigation or Section Heading
    st.subheader("Navigation")
    
    # Interactive Widgets
    selected_page = st.radio("Choose a section", ["Home", "Profile", "Meal History", "Register"])



    # Action Buttons
    if st.button("Logout"):
        st.sidebar.write("Button clicked!")

    # # Use expander for advanced options to keep the sidebar clean
    # with st.expander("Advanced Settings"):
    #     st.checkbox("Enable Advanced Mode")
    #     # More advanced widgets can be placed here

if selected_page == "Home":
    home_page()
elif selected_page == "Profile":
    profile_page()
elif selected_page == "Meal History":
    meal_history_page()
elif selected_page == "Register":
    data, submit_button = registration_page()
    if submit_button:
        with open('userdata.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)

