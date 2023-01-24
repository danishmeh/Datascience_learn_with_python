import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as  px  

# import datset
st.header("gapminder datset")
st.text("we make a graph with the combination of plotly and streamlit")
df = px.data.gapminder()
st.write(df.head())
st.write(df.columns)
st.write(df.describe())

# data management

year_option = df['year'].unique().tolist()
year  = st.selectbox("which year should we plot",year_option,0)
# # df = df[df['year']==year]



continent_n = df['continent'].unique().tolist()
cont = st.selectbox("select Continent",continent_n)
df = df[df['continent']==cont]

st.header("Countinent Graph with Respect to Years")

fig = px.scatter(df,x ='gdpPercap',y ='lifeExp',size ='pop',hover_name='country',color ='country',
                    animation_frame='year',animation_group = 'country',
                    log_x = True, size_max =55,range_x=[100,100000],range_y=[20,90])
fig.update_layout(width=800, height=500)
# HOW TO ANIMATE THE WEBAPP

st.write(fig)
