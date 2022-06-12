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
from app.utils import pg1_head, set_bg

st.set_page_config(
    page_title="Home | Project Portfolio",
    page_icon="random",
    )

pg1_head()

set_bg('assets/app_homepage.jpg')
