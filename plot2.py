import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
# import matplotlib.pyplot as plt

# Altair Scatter plot

st.header("1. Altair Scatter plot")
df = pd.DataFrame(np.random.randn(500,5), columns = ['a','b','c','d','e'])
chart = alt.Chart(df).mark_circle().encode( x = 'a', y = 'b', size = 'c',
        tooltip = ['a','b','c','d','e'])
st.altair_chart(chart)

# line charts
st.header("2. Interactive Charts")
df = pd.read_csv("C:\PYTHON_DS\lang_data.csv")
st.subheader("2.1 Line Chart")
lang_list = df.columns.tolist()
lang_choice = st.multiselect("Choose Your language:", lang_list)
new_df = df[lang_choice]
st.line_chart(new_df)

st.subheader("2.2 Area Chart")
st.area_chart(new_df)

st.header("3. Data Visualization with Plotly")
st.subheader("Displaying the dataset")
df = pd.read_csv('C:\PYTHON_DS\pips.csv')
st.dataframe(df.head())

st.subheader("3.2 Pie Chart")
fig = px.pie(df, values='total_bill', names = 'size')
st.plotly_chart(fig)

st.subheader("3.3 Pie Chart with Multiple Parameters")
fig = px.pie(df, values='total_bill', names = 'day', opacity= .7,
             color_discrete_sequence= px.colors.sequential.RdBu)
st.plotly_chart(fig)


st.subheader('Histogram')
x1 = np.random.randn(200)
x2 = np.random.randn(200)
x3 = np.random.randn(200)

hist_data = [x1,x2,x3]
groups = ['Group-1','Group-2','Group-3']
fig = ff.create_distplot(hist_data, groups, bin_size=[.1,.25,.5])
st.plotly_chart(fig)

