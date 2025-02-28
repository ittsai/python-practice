import streamlit as st
from  send_emails import send_email

st.header("Page 2")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")

    if button:
        send_email()
        st.info("Send email")