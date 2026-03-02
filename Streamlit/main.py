import streamlit as st

x = st.text_input("Favorite Movie?")

st.title(f"Your favorite movie is {x}")