from nbformat import read
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import os
import codecs
import urllib
from streamlit_option_menu import option_menu

@st.cache(suppress_st_warning=True)

def read_data(path):
    return pd.read_csv(path)

#external html file with inline css styling
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
index_page_path = os.path.join(ROOT_DIR, 'html', 'index.html')
index_page_open = open(index_page_path, 'r')
index_page_read = index_page_open.read()

def pg2_header():
    components.html(index_page_read, width=700, height=400, scrolling=True)
    st.write("Hi x")

def pg2_body(sample):
    name = sample.iloc[0, 0]
    link = sample.iloc[0, 1]
    prob = sample.iloc[0, 2]
    st.info(f'### {name}')
    st.write(prob)
    st.caption(f'[source]({link})')
    st.markdown('---')

if st.button('Bring it on!'):
    df = read_data('data/olympiad-problems.csv')
    choice = df.sample(1)
    pg2_body(choice)