
from nbformat import read
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import os
import codecs

@st.cache(suppress_st_warning=True)

def read_data(path):
    return pd.read_csv(path)

index_page_path = "h:\My Drive\Computer_Science_Stuff\RandGenerator\webpage\index.html"
index_page = open(index_page_path, 'r')
index_page_read = index_page.read()

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