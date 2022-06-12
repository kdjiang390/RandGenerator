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
from app.utils import pg2_head, set_bg, pg2_body, pg2_question_generator

st.set_page_config(
    page_title="App 1 | Project Portfolio",
    page_icon="random",
    )

pg2_head()

set_bg('assets/empty_notebook.jpg')

pg2_question_generator()
