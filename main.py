from nbformat import read
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import os
import codecs
import urllib
from streamlit_option_menu import option_menu



st.set_page_config(
    page_title="cool app",
    page_icon="🧊",
    )

@st.cache(suppress_st_warning=True)



st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")
