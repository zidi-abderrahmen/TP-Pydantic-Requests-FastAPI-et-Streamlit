import streamlit as st
import pandas as pd

x = st.text_input("Favorite Movie?")

is_clicked = st.button("Click Me")

st.title(f"Your favorite movie is {x}")


data = pd.read_csv("movies.csv")

st.write(data)