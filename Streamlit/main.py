import streamlit as st
import pandas as pd
import numpy as np

x = st.text_input("Favorite Movie?")

is_clicked = st.button("Click Me")

st.title(f"Your favorite movie is {x}")


data = pd.read_csv("movies.csv")

st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)