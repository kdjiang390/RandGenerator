import streamlit as st
import streamlit_option_menu as option_menu
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
    }
)



def get_data(sometable.csv):
    path = r'some path to concat to the csv'
    return pd.read_csv(path)
df = get_data()

def empty_sidebar():
    with st.sidebar():
        st.title("this is a sidebar title")
        st.write("No parameters available for this page")
        if st.button("Report bug"):
            st.write("insert report bug method")

def parameter_sidebar():
    with st.sidebar():
        st.multiselect(
            "multiselect title",
            pd.DataFrame(),
            "default list of element",
        )
        st.selectbox('selectbox label', ['item 1', 'item 2'], key='1')