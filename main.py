import streamlit as st
import pandas as pd

df = pd.read_csv('data.csv')
d
st.dataframe(df, hide_index=True)