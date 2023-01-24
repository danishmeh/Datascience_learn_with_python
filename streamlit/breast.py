import seaborn as sns 
import pandas as pd
import numpy as np
import matplotlib as plt
import streamlit as st
import plotly.express as px 


st.header("data set loading  diamonds")

df = sns.load_dataset("diamonds")
st.write(df.head())

dat = df['cut'].unique().tolist()
value = st.selectbox("Enter the Cut Techniques",dat,0)
df = df[df['cut']==value]

fig = px.scatter(df, x ='carat',y='depth',color='clarity',
                  
                  hover_name='carat' ,log_x =True)

st.write(fig)