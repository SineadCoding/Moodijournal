import streamlit as st
from textblob import TextBlob
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import random
from pandas.errors import EmptyDataError
from PIL import Image
import os
import nltk


# NLTK_DATA_PATH = os.path.join(os.path.dirname(__file__), "nltk_data")
# if not os.path.exists(NLTK_DATA_PATH):
#     os.makedirs(NLTK_DATA_PATH)
# nltk.data.path.append(NLTK_DATA_PATH)

# @st.cache_resource
# def download_nltk_data():
#     try:
#         nltk.data.find('corpora/brown')
#         st.success("NLTK 'brown' corpus found.")
#     except Exception as e: 
#         st.warning(f"NLTK data not found or an error occurred during check: {type(e).__name__}: {e}. Attempting download...")
#         try:
#             nltk.download('punkt', download_dir=NLTK_DATA_PATH)
#             nltk.download('brown', download_dir=NLTK_DATA_PATH)
#             st.success("NLTK 'punkt' and 'brown' corpora downloaded successfully!")
#         except Exception as download_e: 
#             st.error(f"Failed to download NLTK data: {type(download_e).__name__}: {download_e}")
#             raise download_e


# download_nltk_data()

st.title("MoodiJournal📓")
st.write("Welcome to MoodiJournal, a safe space to write about your day or your feelings throughout the day and assess your mood from a nuetral perpective, "
             " log your mood and content from your journal for you to reflect on and recieve a special message based off of your mood to either support or enhance you day.")
st.write("Happy Journalling!!!🌸")
st.subheader("Write about your day and get insights on your mood.✍🏻")
