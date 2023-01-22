import streamlit as st
import seaborn as sns

st.header("ALLAH")
st.header("My name is Danish Mehmood and learning Streamlit")
st.header("Inshallah I will be a great ML and DS Engineer")
st.header("Inshallah I make a gig on fiver of streamlit")

st.text("Enjoy learning streamlit")

st.text("text is for simple letter")

st.text("now we load data set")
import seaborn as sns
st.header("iris dataset view")
df = sns.load_dataset("iris")
st.text("how to show data set with st.write command")
st.write(df.head())
st.header("MPG dataset show")
st.text("take a 5 sample of MPG dataset")
st.write(df.sample(5))
st.header("Titanic dataset show")
st.text("take a 5 sample of titanic dataset")
df = sns.load_dataset("titanic")
st.write(df.head())

st.header("tips")
df = sns.load_dataset("tips")
st.write(df.head())

st.header("fmri")
fmri = sns.load_dataset("fmri")
st.write(fmri.head())



df = sns.load_dataset("iris")
st.write(df.head())
st.header("testing iris data")
st.write(df[['species','sepal_length']])
st.write(df[['species','petal_length','sepal_length']])
st.write(df[['species','petal_width','sepal_width']])

st.header("bar chart of petal length")
st.bar_chart(df['petal_length'])

st.header("Line Chart")
st.line_chart(df['petal_length'])
st.line_chart(df['petal_width'])
st.line_chart(df['sepal_length'])
st.line_chart(df['sepal_width'])

  