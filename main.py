import streamlit as st

if not st.user.is_logged_in:
    # st.image("images/logo.png", width=200)
    st.title("Welcome to MoodiJournal, the Smart Mood Journal.📓")
    st.subheader("Let's get you signed in!")
    if st.button("Sign in With Google"):
        st.login("google")


else:
    if st.button("Logout"):
        st.logout()
    user_email = st.user.email
    st.title("MoodiJournal📓")
    st.write("Welcome to MoodiJournal, a safe space to write about your day or your feelings throughout the day and assess your mood from a nuetral perpective, "
                     " log your mood and content from your journal for you to reflect on and recieve a special message based off of your mood to either support or enhance you day.")
    st.write("Happy Journalling!!!🌸")
    st.subheader("Write about your day and get insights on your mood.✍🏻")
