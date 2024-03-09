import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

chart = pd.DataFrame(np.random.randn(20,3), columns=['Line-1','Line-2','Line-3'])
# all the below plots are interactive
# Line chart --------------------------------------------------------------
st.header("1. Charts with Random Numbers")
st.subheader("1.1 Line Chart")
st.line_chart(chart)

# Area chart ----------------------------------------------------------------------
st.subheader("1.2 Area Chart")
st.area_chart(chart)

# Bar chart ----------------------------------------------------------------------
st.header("1.3 Bar Chart")
st.bar_chart(chart)
#------------------------------------------------------------------------------------
st.header("2. Data Visualization with Matplotlib and seaborn")  
st.subheader("2.1 Loading the dataframe")
df = pd.read_csv("C:\PYTHON_DS\iris.csv")
st.dataframe(df)

st.subheader("2.2 Bar Graph with Matplotlib")
fig = plt.figure(figsize = (15,8))
df["species"].value_counts().plot(kind = "bar")
st.pyplot(fig)

st.subheader("2.3 Distribution Plot with Seaborn")
fig = plt.figure(figsize = (15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header("3 Working with multiple graphs in one column")
# st.header("3 Working with multiple graphs")

col1, col2 = st.columns(2)
with col1:
    col1.header = 'KDE = False'
    # st.write("KDE = False")
    fig1 = plt.figure(figsize=(4,4))
    #kde = True just adds a line on the distplot
    sns.distplot(df['sepal_length'], kde=False)
    st.pyplot(fig1)

with col2:
    col2.header = 'hist = False'
    
    fig2 = plt.figure(figsize=(4,4))
    #hist = True just adds the histogram behind the line(kde) in the distplot
    sns.distplot(df['sepal_length'], hist=False)
    st.pyplot(fig2)
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
st.header("4. Changing style")

col1, col2 = st.columns(2)
with col1:
    col1.header = 'KDE = False'
    sns.set_style('darkgrid')
    sns.set_context("notebook")#context must be in paper, notebook, talk, poster
    sns.distplot(df['sepal_length'], hist=False)
    st.pyplot(fig1)

with col2:
    col2.header = 'hist = False'
    sns.set_theme(context='poster', style='darkgrid')
    sns.distplot(df['sepal_length'], hist=False)
    st.pyplot(fig2)
    
    
st.header("5. Exploring Different graphs")
st.subheader('5.1 Scatter plot')
fig, ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.randn(2,100))
st.pyplot(fig)
#--------------------------------------------------------------------------------------------------------
st.subheader('5.1 Count-plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data= df, x = 'species')
st.pyplot(fig)



st.subheader('5.1 Box-plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data= df, x = 'species', y = 'petal_length')
st.pyplot(fig)


st.subheader('5.1 Violin-plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data= df, x = 'species', y = 'petal_length')
st.pyplot(fig)





