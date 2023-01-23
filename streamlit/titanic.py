import streamlit as st
import seaborn as sns
from sklearn.linear_model import LinearRegression
from  sklearn.ensemble  import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

from sklearn.metrics import mean_squared_error

# make containers
header = st.container()
data_set = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Kashti ki app")
    st.text("in this project we will work on kashti datset")
    
with data_set:
    st.header("kashti doob gayi"" hahaa")
    df = sns.load_dataset("titanic")
    df = df.dropna()
    st.write(df.head())
    
    st.header("bar chart") 
    st.bar_chart(df['age'].value_counts())
    
    st.header("Gender count")
    st.bar_chart(df['sex'].value_counts())
    
    st.header("Class count")
    st.bar_chart(df['class'].value_counts())  
    
with features:
    
    st.header("this is the feature app of Boat")
    # st.write(df.columns)
    X = df[['age']]
    y = df[['fare']]
    
with model_training:
    st.header("kashti walo ka kyia bna model training")
    # making columns selection and display columns
    input,display = st.columns(2)
    
    max_depth = input.slider("how many person du you want to select",min_value =10,max_value=150,value =20,step=10)
    n_estimators = input.selectbox("how many Tree we want to Enter",options={50,100,150,200,'Null_Value'})
    # Adding Features
    input.write(df.columns)
    
    # input features are taken from users
    input_features = input.text_input("features are taken from user") 
    # test = input.text_input("Enter Class of Passenger")
    # gend = input.text_input("Enter the sex of data")
    
  
    #  # X and y define
    X = df[[input_features]]
    y = df[['fare']]
    model = RandomForestRegressor(max_depth=max_depth,n_estimators=n_estimators)
    model.fit(X, y)
    pred = model.predict(y)
    
     # Display metrics
    display.subheader('mean absolute error of the model is',)
    display.write(mean_squared_error(y,pred))
    
    
    
    
    
    
    
    # test = input.slider("Class Enter", min_value=0,max_value=3,step=1,value=1)
    # fare = input.slider("fare enter",min_value=0,max_value=1500,value=100,step=100)
    # age = input.slider("age Select",min_value=14,max_value=110,step=10,value=50)
 
    
    
    