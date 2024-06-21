import streamlit as st
import send_email as mail

st.header("Contact Sam Ervin")

st.subheader("Please fill out the form below to contact Sam.")

with st.form(key='contact_form'):
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Submit")

    if submitted:
        if(user_email == "" or message == ""):
            st.warning("Please fill out the form.")
        else:
            mail.send_mail(user_email, "Contact Form", message)
            st.success("Thank you for your Message. It was sent successfully! Sam will get back to you soon.")
            st.balloons()