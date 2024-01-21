from imports import *


def fade_in(element, duration=0.5):
    start_time = time.time()
    while time.time() - start_time < duration:
        alpha = min(1.0, (time.time() - start_time) / duration)
        st.markdown(f'<div style="opacity: {alpha};">{element}</div>', unsafe_allow_html=True)
        time.sleep(0.01)

# Backend functions to generate content
def get_random_content():
    # This function simulates getting content from the backend.
    # Replace this with actual backend logic (e.g., database query, API call).
    phrases = ["Hello, World!", "Streamlit is Awesome!", "Dynamic Content Here!"]
    return random.choice(phrases)

def update_content_from_backend():
    for box_num in range(1, 4):
        st.session_state[f'content_box{box_num}'] = get_random_content()

def meal_time(current_datetime):
    current_time = current_datetime.time()
    breakfast_start = time(7, 0)  # 7:00 AM
    breakfast_end = time(10, 0)   # 10:00 AM

    lunch_start = time(12, 0)     # 12:00 PM
    lunch_end = time(14, 0)       # 2:00 PM

    dinner_start = time(18, 0)    # 6:00 PM
    dinner_end = time(21, 0) 
    
    mealtime = None

    if breakfast_start <= current_time <= breakfast_end:
        mealtime = "Breakfast"
    elif lunch_start <= current_time <= lunch_end:
        mealtime = "Lunch"
    elif dinner_start <= current_time <= dinner_end:
        mealtime = "Dinner"

    return mealtime

def home_page():
    current_datetime = datetime.now()
    for box_num in range(1, 4):
        if f'content_box{box_num}' not in st.session_state:
            st.session_state[f'content_box{box_num}'] = 'Click "Update Content" to generate content.'

    if meal_time(current_datetime):
        st.title(f"Welcome, its time for {meal_time(current_datetime)}!")
    else:
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

    st.markdown('''
                <div style="display: flex; padding: 20px; justify-content: center;">
                    <button type="button" class="btn btn-outline-success btn-lg">EAT NOW</button>
                </div>
                ''', unsafe_allow_html=True) 

    st.markdown('''
                <div style="display: flex; padding: 20px; justify-content: center;">
                    <button type="button" class="btn btn-outline-danger btn-lg">REPLAN</button>
                </div>
                ''', unsafe_allow_html=True) 


    # st.markdown"EAT NOW", key = "eat_now", **{'class': 'big-button'})
    # st.button("REPLAN", key = 'replan', **{'class' : 'big-button'})

def profile_page():
    pass

def hash_password(password):
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the password bytes
    sha256.update(password.encode('utf-8'))

    # Get the hexadecimal representation of the hashed password
    hashed_password = sha256.hexdigest()

    return hashed_password

def registration_page():
    st.title("Profile Page")

    st.header('Basic Information', divider='rainbow')
    username = st.text_input("Username: ")
    password = st.text_input("Password: ")
    pass2 = st.text_input("Repeat Password: ")
    name = ''
    age = 0
    gender = None
    preference = None
    weight =None
    height =None
    option= None
    selected_option = None
    hashed_password = None
    if username and password and password==pass2:
        hashed_password = hash_password(password)

        # Step 1: Ask for the name
        with st.chat_message("user"):
            st.write("Hello 👋, What shall we call you?")
            name = st.text_input('')
            if name:
                st.write("Hi,", name, "Welcome!")

        # Step 2: Ask for the age
        if name:
            with st.chat_message("user"):
                st.write(name, " please enter your age")
                age = st.number_input('',placeholder='')

        # Step 3: Ask for gender and preference
        if age:
            with st.chat_message("user"):
                st.write("Aah!! More radio boxes!!!")
                with st.container():
                    col1, col2 = st.columns(2)  # Create two columns

                    with col1:
                        gender = st.radio("Gender", ["Male", "Female"],index=None)

                    with col2:
                        preference = st.radio("Meal Preference", ["Veg", "Non Veg"],index=None)

        # Step 4: Ask for height and weight
        if gender is not None and preference is not None:
            with st.container():
                col1, col2 = st.columns(2)  # Create two columns

                with col1:
                    height = st.number_input('Enter Height in cm.', value=None, placeholder="180")

                with col2:
                    weight = st.number_input('Enter Weight in kg.', value=None, placeholder="70")
        cq=0
        if weight !=None and height !=None:
            with st.chat_message("user"):
                yes = st.toggle('Any prevalant medical conditions ?')
                if yes:
                    option = st.selectbox('Please select from the following:',('...', 'High Blood Pressure', 'Cardiovascular Diseases', 'Diabetes','Other'),index=None)
                    if option =='Other':
                        option = st.text_input('',placeholder="Please descibe your medical condition")
                else:
                    option = 'NA'
                cq=1
        if cq :
            with st.chat_message("user"):
                st.write("Please select one of the following target")
                options = ["Muscle Gain", "Weight Loss", "Weight Gain", "Regular Diet"]
                col1, col2, col3, col4 = st.columns(4)  # Adjust the number of columns based on your needs

                selected_option_1 = col1.button(options[0], key=options[0])  # Default selection
                selected_option_2 = col2.button(options[1], key=options[1])
                selected_option_3 = col3.button(options[2], key=options[2])
                selected_option_4 = col4.button(options[3], key=options[3])
                
        # Show the selected option
                if selected_option_1 or selected_option_2 or selected_option_3 or selected_option_4:
                    selected_option = (
                        options[0] if selected_option_1
                        else options[1] if selected_option_2
                        else options[2] if selected_option_3
                        else options[3]
                    )
    all_filled = all([name, username, hashed_password, age, gender, preference, height, weight, option, selected_option])
    submit_button = False
    if name != '' and age > 0 and gender!= None and preference!=None and weight !=None and height != None and option != None and selected_option != None and hashed_password != None:
        submit_button = st.button("Submit")
        submit_button = True
    print(submit_button)
    return [name, username, hashed_password, age, gender, preference, height, weight, option, selected_option], submit_button

def check_credentials(username, password, file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                return True
        return False

def login():
    st.header(':blue[Dinewise] AI',divider="rainbow")
    st.subheader('Login')
    name = st.text_input('', placeholder='Username')
    password = st.text_input('', type='password',placeholder='Password')
    if name and password and check_credentials(name, password, "userdata.csv"):
        home_page()
    st.write('Not registerd yet ? Register Here: __')

def meal_history_page():
    st.title("Meal History Page")
    # Add content for the Meal History Page