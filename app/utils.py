from email.base64mime import decode
from nbformat import read
import base64
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import os
import codecs
import urllib
from streamlit_option_menu import option_menu


@st.cache(suppress_st_warning=True)

def header_html():
    current_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    target_path = os.path.join(current_path, 'html', 'index.html')
    with open(target_path,"r") as opened_path:
        read_path = opened_path.read()
    components.html(read_path, width=500, height=500)

def head():
    st.markdown("test line")
    st.write("something")

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
        background-attachment: scroll;
        }
        </style>
    """ % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)