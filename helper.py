from imports import *
from calorie_req import *
from model import *

def fade_in(element, duration=0.5):
    start_time = time.time()
    while time.time() - start_time < duration:
        alpha = min(1.0, (time.time() - start_time) / duration)
        st.markdown(f'<div style="opacity: {alpha};">{element}</div>', unsafe_allow_html=True)
        time.sleep(0.01)

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

def fetch_data(username, file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == username:
                return row
        return None

def home_page():
    if 'username' not in st.session_state:
        # Handle the case where the username is not set, perhaps redirect to login page
        st.warning("Please log in first.")
        return None  # or you could return a redirect to a login page or a default value


    current_datetime = datetime.now()
    with open("session.txt", 'r') as file:
        username = file.read()
    data = fetch_data(username, 'userdata.csv')
    x = data[5]
    is_veg = True
    if data[5] == 'Veg':
        is_veg = True
    else:
        is_veg = False


    if 'responses' not in st.session_state:
        try:
            st.session_state['responses'] = get_model_response(
                data[9], 1, data[3], data[8], data[7], data[4], data[6], is_veg, None, data[11], None)
        except KeyError:
            st.session_state['responses'] = ["Sample Content cuz key ran out credits :("] * 3

    responses = st.session_state['responses']
    print(responses[0])
    print(type(responses[0]))
    
    
    # if 'home_displayed' not in st.session_state:
    #     st.session_state['home_displayed'] = True
    if meal_time(current_datetime):
        st.title(f"Welcome, it's time for {meal_time(current_datetime)}!")
    else:
        st.title("Welcome!")

    # Create and display columns for meals
    col1, col2, col3 = st.columns(3)
    meals = ['BreakFast', 'Lunch', 'Dinner']
    for i, col in enumerate([col1, col2, col3]):
        with col:
            meal = meals[i]
            st.subheader(meal)
            content_key = f'content_box{i + 1}'
            st.session_state[content_key] = "Click below to get your suggested meal"
            st.write(st.session_state[content_key])
            if (st.button("View Meal details", key=meal.lower())):
                with st.expander(meals[i], expanded=True):
                    st.write(responses[i])
            
    # try:
    #     responses = get_model_response(data[9], 1, data[3], data[8], data[7], data[4], data[6], is_veg, None, data[11], None)
    #     for box_num in range(1, 4):
    #         print(responses)
    #         if f'content_box{box_num}' not in st.session_state:
    #             meal_name = responses[box_num-1]
    #             desc = None
    #             try:
    #                 desc = responses[box_num-1]
    #             except:
    #                 pass
    #             st.session_state[f'content_box{box_num}'] = meal_name + desc
    # except KeyError:
    #     for box_num in range(1, 4):
    #         if f'content_box{box_num}' not in st.session_state:
    #             st.session_state[f'content_box{box_num}'] = "Sample Content cuz key ran out credits :("



    
    col1, col2, col3 = st.columns([1,2,1])

        
    st.write("Didn't Like the suggestions? Regenerate them by clicking here")
    if st.button("Regenerate"):
         if 'responses' in st.session_state:
            del st.session_state['responses']
            st.experimental_rerun()
            home_page()


    # breakfast = st.session_state['content_box1']
    # lunch = st.session_state['content_box2']
    # dinner = st.session_state['content_box3']
    # progress_bar = st.progress(0)
    # net_calories = 0.0
    # try:
    #     if(st.session_state['content_box1']):
    #         net_calories += breakfast['Calories']
    #     if(st.session_state['content_box2']):
    #         net_calories += lunch['Calories']
    #     if(st.session_state['content_box3']):
    #         net_calories += dinner['Calories']
    # except:
    #     pass
    # info = []
    
    # info, button = registration_page()
    # age = info[3]
    # gender = info[4]
    # physical_activity = info[6] 
    # height = info[7]
    # weight = info[8]
    # calories_req = total_energy_req(age, weight, height, gender, physical_activity)

    # st.write("Progress made so far:")
    # progress_bar.progress(net_calories/calories_req)
    # st.markdown"EAT NOW", key = "eat_now", **{'class': 'big-button'})
    # st.button("REPLAN", key = 'replan', **{'class' : 'big-button'})


def create_card(title, content, icon):
    card_html = f"""
    <div class="card">
        <div class="card-content">
            <span class="card-icon"><i class="{icon}"></i></span>
            <span class="card-title">{title}</span>
            <span class="card-detail">{content}</span>
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

def profile_page():
    st.markdown("""
    <script src="https://kit.fontawesome.com/70a73d985d.js" crossorigin="anonymous"></script>
    <style>
    /* Main card layout */
    .card {
        margin: 10px;
        padding: 20px;
        border-radius: 15px;
        color: #ffffff;
        background: #1e1e1e;
        box-shadow: 0px 0px 10px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
    }

    /* Hover effect for card */
    .card:hover {
        transform: translateY(-5px);
    }

    /* Card content styling */
    .card-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    /* Icon styling */
    .card-icon {
        font-size: 2em;
        margin-bottom: 5px;
    }

    /* Title styling */
    .card-title {
        font-size: 1em;
        font-weight: bold;
        margin-bottom: 5px;
    }

    /* Detail text styling */
    .card-detail {
        font-size: 1.2em;
        font-weight: bold;
    }

    /* Responsive grid layout */
    @media (min-width: 800px) {
        .stButton > button {
            width: 100%;
        }
        .stTextInput > div > div > input {
            width: 100%;
        }
        .stSelectbox > div {
            width: 100%;
        }
        .stDateInput > div > input {
            width: 100%;
        }
    }
    </style>
    """, unsafe_allow_html=True)


    with open('session.txt', 'r') as file:
        username = file.read()
    print("username: :", username)
    filepath = 'userdata.csv'
    row = fetch_data(username, filepath)
    if row:
    # Extract user data
        name, age, gender, preference, phy, height, weight, t_weight, medical_condition, target = row[0], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]
        
        # Display user's name as main title
        st.markdown(f"<h1>Hello! <span style='color:dodgerblue;'>{name}</span></h1>", unsafe_allow_html=True)
        
        # Create a two-column layout for cards
        col1, col2 = st.columns(2)
        
        with col1:
            create_card("Age", age, "fas fa-birthday-cake")
            create_card("Gender", gender, "fas fa-venus-mars")
            create_card("Preference", preference, "fas fa-utensils")
            create_card("Physical Activity Level", phy, "fas fa-bicycle")
            create_card("Target", target, "fas fa-flag-checkered")
        
        with col2:
            create_card("Height", f"{height} cm", "fas fa-ruler-vertical")
            create_card("Weight", f"{weight} kg", "fas fa-weight")
            create_card("Target Weight", f"{t_weight} kg", "fas fa-bullseye")
            create_card("Medical Condition", medical_condition, "fas fa-notes-medical")
        
    else:
        st.error("User not found.")


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
    target_weight = 0
    physical_activity = None
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
                    col1, col2, col3 = st.columns(3)  # Create two columns

                    with col1:
                        gender = st.radio("Gender", ["Male", "Female"],index=None)

                    with col2:
                        preference = st.radio("Meal Preference", ["Veg", "Non Veg"],index=None)
                    with col3:
                        physical_activity = st.radio("Physical Activity Level", ["Sedentary", "Low Active", "Active", "Other"], index = None)

        # Step 4: Ask for height and weight
        if gender is not None and preference is not None:
            with st.container():
                col1, col2, col3 = st.columns(3)  # Create two columns

                with col1:
                    height = st.number_input('Enter Height in cm.', value=None, placeholder="180")

                with col2:
                    weight = st.number_input('Enter Weight in kg.', value=None, placeholder="70")
                with col3:
                    target_weight = st.number_input('Enter Target Weight in kg.', value = None, placeholder="65")

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
                options = ["Muscle Gain", "Weight Loss", "Weight Gain", "Regular Diet"]
                col1, col2, col3, col4 = st.columns(4)  # Adjust the number of columns based on your needs

                selected_option = st.radio("Please select one of the following target", options,index=None)
        #         selected_option_1 = col1.button(options[0], key=options[0])  # Default selection
        #         selected_option_2 = col2.button(options[1], key=options[1])
        #         selected_option_3 = col3.button(options[2], key=options[2])
        #         selected_option_4 = col4.button(options[3], key=options[3])
                
        # # Show the selected option
        #         if selected_option_1 or selected_option_2 or selected_option_3 or selected_option_4:
        #             selected_option = (
        #                 options[0] if selected_option_1
        #                 else options[1] if selected_option_2
        #                 else options[2] if selected_option_3
        #                 else options[3]
                    # )
    st.session_state['username'] = username
    l =[name, username, hashed_password, age, gender, preference, physical_activity, height, weight, target_weight, option, selected_option]
    submit_button = False
    if name != '' and age > 0 and gender!= None and preference!=None and weight !=None and height != None and option != None and selected_option != None and hashed_password != None and physical_activity != None and target_weight > 0:
        submit = st.button("Submit")
        submit_button = True

    print(l)
    print(submit_button)
    print("test")
    return l, submit_button

def check_credentials(username, password, file_path):
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == username and row[2] == password:
                return True
        return False

def login():
    st.header(':blue[Dinewise] AI',divider="rainbow")
    st.subheader('Login')
    name = st.text_input('', placeholder='Username')
    password = st.text_input('', type='password',placeholder='Password')
    if name and password and check_credentials(name, hash_password(password), "userdata.csv"):
        st.session_state['username'] = name
        with open("session.txt", "w") as file:
            file.write(name)
        return True
    st.write('Not registerd yet ? Register Here:')
    if st.button("Register"):
        st.session_state['registration_page'] = True
