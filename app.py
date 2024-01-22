from calorie_req import *
from imports import *
from recipes import *
from helper import *
from model import *


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


if 'registration_page' not in st.session_state:
    st.session_state['registration_page'] = False

if 'login_page' not in st.session_state:
    st.session_state['login_page'] = True

if 'is_logged_in' not in st.session_state:
    st.session_state['is_logged_in'] = False

# Conditional rendering based on the session state
if not st.session_state['is_logged_in']:
    if st.session_state['login_page']:
        # Show the login form
        if login():
            # If login is successful, hide the login page and show the home page
            st.session_state['login_page'] = False
            st.session_state["is_logged_in"] = True

            st.experimental_rerun()

        # If login is not successful, the login page remains visible

if st.session_state['registration_page']:
    # Show the registration form
    data, submit_button = registration_page()
    if submit_button:
        with open('userdata.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(data)


if st.session_state['is_logged_in']:    
    # Layout of the sidebar
    with st.sidebar:
        st.title("Control Panel")

        # Navigation or Section Heading
        st.subheader("Navigation")
        
        # Interactive Widgets
        selected_page = st.radio("Choose a section", ["Home", "Profile", "Register"])



        # Action Buttons
        if st.button("Logout"):
            st.session_state['login_page'] = True
            st.session_state['registration_page'] = False
            st.session_state['is_logged_in'] = False
        # # Use expander for advanced options to keep the sidebar clean
        # with st.expander("Advanced Settings"):
        #     st.checkbox("Enable Advanced Mode")
        #     # More advanced widgets can be placed here
            
    if selected_page == "Home":
        home_page()
        

    elif selected_page == "Profile":
        profile_page()
    elif selected_page == "Register":
        data, submit_button = registration_page()
        if submit_button:
            with open('userdata.csv', 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(data)

