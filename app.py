import streamlit as st

def on_submit():
    st.write("Submit button clicked!")

def main():
    # Create a text input field
    text_input = st.text_input("Enter your text", key='text_input')

    # Add a submit button
    submit_button = st.button("Submit")

    # Check if Enter key is pressed in the text input field
    if text_input and st.session_state.text_input != text_input:
        st.session_state.text_input = text_input
        submit_button.click()

    # Register the submit button's click event
    submit_button.clicked = on_submit()

if __name__ == '__main__':
    main()
