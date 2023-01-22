

import pandas as pd
import streamlit as st
import seaborn as sns
from  sklearn.ensemble  import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score




# make Containers
header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.header("Titanic app")
    st.text("we are going to analysis on titanic datasets")
    
with dataset:
    st.header("Boat get sunck down")
    st.text(" boat Analyst")
    # import dataset using seaborn
    df = sns.load_dataset("titanic")
    st.write(df.head())
    df = df.dropna() 
    st.subheader("Gender Count")
    st.bar_chart(df['sex'].value_counts())
    st.subheader("Class Count")
    st.bar_chart(df['class'].value_counts())
    # age chart
    st.subheader("passengers Count with respect to age") 
    st.bar_chart(df['age'].value_counts())
    # 
    st.bar_chart(df['age'].sample(5))

with features:
    st.header("This is our app feature")
    st.text("important features checked")
    st.text(df.columns)
    
with model_training:
    st.header("Trained model using ML")
    # making columns selection and display columns
    input,display = st.columns(2)
    # first column include selection points
    
    max_depth =input.slider("how many peoples do you know",min_value=10,max_value=100,value=20,step =5)

    n_estimators =input.selectbox("how many tree be there",
                                 options = [50,100,150,200,'nolimit'])
    # adding list of features
    input.write(df.columns)
    # input features from users
    input_features = input.text_input("Which features we can use")
     
     # machine learning model
    model = RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)
    # drop nan values
    
    #  # X and y define
    X = df[[input_features]]
    y = df[['fare']]
    model.fit(X, y)
    pred = model.predict(y)
    
    # Display metrics
    display.subheader('mean absolute error of the model is',)
    display.write(mean_absolute_error(y,pred))
    display.subheader('mean squared error of the model is',)
    display.write(mean_squared_error(y,pred))
    display.subheader('r2 squared scored of the model is',)  
    display.write(r2_score(y,pred))   