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


NLTK_DATA_PATH = os.path.join(os.path.dirname(__file__), "nltk_data")
if not os.path.exists(NLTK_DATA_PATH):
    os.makedirs(NLTK_DATA_PATH)
nltk.data.path.append(NLTK_DATA_PATH)

@st.cache_resource
def download_nltk_data():
    try:
        nltk.data.find('corpora/brown', paths=[NLTK_DATA_PATH])
    except nltk.downloader.DownloadError:
        st.warning("NLTK data not found, attempting download...")
        try:
            nltk.download('punkt', download_dir=NLTK_DATA_PATH)
            nltk.download('brown', download_dir=NLTK_DATA_PATH)
            st.success("NLTK data downloaded successfully!")
        except Exception as e:
            st.error(f"Failed to download NLTK data: {e}")
            raise e
    except Exception as e: 
        st.error(f"An unexpected error occurred while checking NLTK data: {e}")
        raise e

download_nltk_data()


st.title("MoodiJournal📓")
st.write("Welcome to MoodiJournal, a safe space to write about your day or your feelings throughout the day and assess your mood from a nuetral perpective, "
                 " log your mood and content from your journal for you to reflect on and recieve a special message based off of your mood to either support or enhance you day.")
st.write("Happy Journalling!!!🌸")
st.subheader("Write about your day and get insights on your mood.✍🏻")
