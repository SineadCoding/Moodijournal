import streamlit as st
from textblob import TextBlob
import pandas as pd
import datetime



st.set_page_config(page_title="MoodiJournal", page_icon="😊", layout="centered")

if 'journal_entries' not in st.session_state:
    st.session_state.journal_entries = []

st.sidebar.header("Debugging Controls")
st.sidebar.markdown("Toggle sections to test your app bit by bit.")

enable_header_section = st.sidebar.checkbox("Enable Header & Intro", True)
enable_input_section = st.sidebar.checkbox("Enable User Input", True)
enable_analysis_section = st.sidebar.checkbox("Enable Mood Analysis", True)
enable_save_section = st.sidebar.checkbox("Enable Save & Past Entries", True)

st.sidebar.markdown("---")
st.sidebar.info("If your app crashes, try disabling sections one by one from top to bottom to isolate the problematic part.")

if enable_header_section:
    st.title("MoodiJournal - Your Daily Mood Tracker")
    st.markdown("Welcome to MoodiJournal! Reflect on your day and let's analyze your mood.")
    st.markdown("---") # Visual separator

user_text = "" 
if enable_input_section:
    st.subheader("How are you feeling today?")
    user_text = st.text_area("Write about your day:", height=200, key="mood_input_area")







# st.title("MoodiJournal📓")
# st.write("Welcome to MoodiJournal, a safe space to write about your day or your feelings throughout the day and assess your mood from a nuetral perpective, "
#                  " log your mood and content from your journal for you to reflect on and recieve a special message based off of your mood to either support or enhance you day.")
# st.write("Happy Journalling!!!🌸")
# st.subheader("Write about your day and get insights on your mood.✍🏻")
