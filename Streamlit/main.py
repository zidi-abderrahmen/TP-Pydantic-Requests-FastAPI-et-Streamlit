import streamlit as st

x = st.text_input("Favorite Movie?")

is_clicked = st.button("Click Me")

st.title(f"Your favorite movie is {x}")