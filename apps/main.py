import streamlit as st
from utils import read_data, head, body

head()

if st.button('Bring it on!'):
    df = read_data('data/olympiad-problems.csv')
    choice = df.sample(1)
    body(choice)