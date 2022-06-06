
from nbformat import read
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import os
import codecs
import urllib

@st.cache(suppress_st_warning=True)

def read_data(path):
    return pd.read_csv(path)

#method 1 - PICK 1 OF THE 2 DON'T RUN BOTH
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
index_page_path = os.path.join(ROOT_DIR, 'webpage', 'index.html')
index_page_open = open(index_page_path, 'r')
index_page_read = index_page_open.read()

#method 1 - PICK 1 OF THE 2 DON'T RUN BOTH
index_page_link = "https://github.com/kdjiang390/RandGenerator/blob/45e1216f5f399f7aa26e029c4d8b970b15806501/webpage/index.html"
#index_page = open(index_page_link, 'r')
index_page_urlopen = urllib.urlopen(index_page_link)
index_page_read = index_page_urlopen.read()


def head():
    
    components.html(index_page_read, width=700, height=400, scrolling=True)
    
    st.write("Hi x")

def body(sample):
    name = sample.iloc[0, 0]
    link = sample.iloc[0, 1]
    prob = sample.iloc[0, 2]
    st.info(f'### {name}')
    st.write(prob)
    st.caption(f'[source]({link})')
    st.markdown('---')