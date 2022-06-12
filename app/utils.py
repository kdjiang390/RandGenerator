from nbformat import read
import base64
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
import os
import codecs
import urllib
from streamlit_option_menu import option_menu


@st.cache(suppress_st_warning=True)

#making the dataframe
def read_data(path):
    return pd.read_csv(path)
def path_find(csvfile): 
    current_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    target_path = os.path.join(current_path, 'data', csvfile)
    return target_path
df = read_data(path_find('olympiad-problems.csv'))

#embedding external html
#not used yet, just an idea
def header_html():
    current_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    target_path = os.path.join(current_path, 'html', 'index.html')
    with open(target_path,"r") as opened_path:
        read_path = opened_path.read()
    components.html(read_path, width=500, height=500)
#first page header
def pg1_head():
    st.markdown("""
        <h1 style='text-align: center;
        align-items: center;
        letter-spacing: 20px;
        font-size: 50px;
        white-space: normal;
        word-break:break-word;
        padding: 10px;
        margin-top: 80px;
        margin-left: 20px;
        margin-right: 20px;
        border: solid;
        '>
        PROJECT PORTFOLIO
        </h1>
    """, unsafe_allow_html=True
    )
    
    st.caption("""
        <p style='text-align: center;
        color: white;
        padding-top: 10px;
        '>
        By <a href='https://kdjiang390.github.io/'>Kenneth Jiang</a>
        </p>
    """, unsafe_allow_html=True
    )
    
    st.markdown("""
        <p style='text-align: center'>
        Welcome! Please feel free to check out the projects I've been working on.
        <br>
        Click the menu on the left to get started. :)
        </p>
    """, unsafe_allow_html=True 
    )
    
    st.caption("""
        <p style='text-align: center;'>
        Background artwork by <a href="https://www.freepik.com/vectors/memphis-shapes">starline</a>
        </p>
    """, unsafe_allow_html=True
    )

#using an external image as background
@st.cache(allow_output_mutation=True)

def get_base64(asset_file):
    with open(asset_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg(background):
    bin_str = get_base64(background)
    page_bg_img = """
        <style>
        .stApp {
        background-image: url("data:image/jpg.jpg;base64,%s");
        background-size: cover;
        background-position: center;
        background-attachment: scroll;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

#pg 2 - making the random question generator

def pg2_head():
    st.markdown("""
        <h1 style='text-align: center;
        align-items: center;
        font-size: 50px;
        white-space: normal;
        word-break:break-word;
        padding: 10px;
        margin-top: 0px;
        margin-left: 20px;
        margin-right: 20px;
        '>
        Math Olympiad Problem Generator
        </h1>
    """, unsafe_allow_html=True
    )
    
    
    st.markdown("""
        <p style='text-align: center'>
        Click the botton below to get started!
        </p>
    """, unsafe_allow_html=True 
    )
    
    st.caption("""
        <p style='text-align: center;'>
        Background artwork by <a href="https://unsplash.com/photos/UrafSwRu3hk?utm_source=unsplash&utm_medium=referral&utm_content=creditShareLink">Kelly Sikkema</a>
        </p>
    """, unsafe_allow_html=True
    )

def pg2_body(sample):
    name = sample.iloc[0, 0]
    link = sample.iloc[0, 1]
    prob = sample.iloc[0, 2]
    Q_info = st.info(f'### {name}')
    Q_problem = st.write(prob)
    Q_caption = st.caption(f'[source]({link})')
    st.markdown('---')

def pg2_question_generator():
    col1, col2, col3 , col4, col5, col6, col7 = st.columns(7)
    with col1:
        pass
    with col2:
        pass
    with col3 :
        pass
    with col4:
        gen_button = st.button('Hit me')
    with col5:
        pass
    with col6:
        pass
    with col7:
        pass
    if gen_button:
        choice = df.sample(1)
        pg2_body(choice)
#pg3 - showing data used

def pg3_explanation(df):
    st.header('Display Player Stats of Selected Team(s)')
    st.write('Data Dimension: ' + str(df.shape[0]) + ' rows and ' + str(df.shape[1]) + ' columns.')
    st.dataframe(df)


def pg3_filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="olympiad-problems.csv">Download CSV File</a>'
    return href
def pg3_download_button():    
    st.markdown(pg3_filedownload(df), unsafe_allow_html=True)