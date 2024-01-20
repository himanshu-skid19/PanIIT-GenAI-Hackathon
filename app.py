import streamlit as st


def get_model_response():
    pass

st.title("Making India Fit")

if 'history' not in st.session_state:
    st.session_state['history'] = []

user_message = st.text_input("Your Message", key="input")

if st.session_state.input:
    st.session_state.history.append("You: " + user_message)

    response = get_model_response(user_message)

    st.session_state.history.append("Mixtral: " + response)

    st.session_state.input = ""

for message in st.session_state.history:
    st.text(message)
    