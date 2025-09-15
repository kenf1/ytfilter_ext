import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Basic Dashboard", page_icon="📊", layout="wide")

st.title("Basic Streamlit Dashboard")
st.sidebar.header("Controls")

# sidebar widgets
num = st.sidebar.slider("Select a number", 1, 100, 10)
st.sidebar.markdown("Customize your dashboard using widgets!")

df = pd.DataFrame({"x": range(1, num + 1), "y": [i**2 for i in range(1, num + 1)]})

st.write("## Data Table")
st.dataframe(df)

st.write("## Chart")
chart = alt.Chart(df).mark_line().encode(x="x", y="y")
st.altair_chart(chart, use_container_width=True)
