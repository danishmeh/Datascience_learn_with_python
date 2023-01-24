import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px  


st.header("mpg data format")
df = sns.load_dataset("mpg")
st.write(df.head())

st.write(df.describe())

# make a select box of origin
# origin = df['origin'].unique().tolist()
# select = st.selectbox("Select the origin",origin)
# df = df[df['origin']==select]

# model_year = df['model_year'].unique().tolist()
# model = st.selectbox("Model_year",model_year)
# df = df[df['model_year']==model]

fig = px.scatter(df, x='model_year',y ='weight',color ='origin',
                 size = 'weight',
                 hover_name='weight',
                 range_x=[70,82],range_y=[1613,5140],
                 animation_frame='mpg',animation_group = 'origin')
fig.update_layout(width =800,height =400)
st.write(fig)

figg = px.line(df,x ='mpg',y='acceleration',color ='origin')
st.write(figg)

