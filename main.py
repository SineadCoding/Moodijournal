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


@st.cache_resource
def download_nltk_data():
    try:
        nltk.data.find('corpora/brown') 
    except nltk.downloader.DownloadError:
        nltk.download('punkt')
        nltk.download('brown') 

download_nltk_data()


st.title("MoodiJournal📓")
st.write("Welcome to MoodiJournal, a safe space to write about your day or your feelings throughout the day and assess your mood from a nuetral perpective, "
                 " log your mood and content from your journal for you to reflect on and recieve a special message based off of your mood to either support or enhance you day.")
st.write("Happy Journalling!!!🌸")
st.subheader("Write about your day and get insights on your mood.✍🏻")
