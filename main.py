from nbformat import read
import base64
import pandas as pd
from requests import head
import streamlit as st
import streamlit.components.v1 as components
import os
import codecs
import urllib
from streamlit_option_menu import option_menu
from app.utils import header_html
from app.utils import set_bg
from app.utils import head

st.set_page_config(
    page_title="cool app",
    page_icon="🧊",
    )
head()
header_html()
#set_bg('assets/mac-at-desk.jpg') dont use because it blocks the html run
