import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn import datasets 
from sklearn.model_selection import train_test_split
from sklearn.decomposition import  PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.write(''' 
         #  Explore Different ML Model with **web_APP**''')
# now we add box and select dataset
dataset_name = st.sidebar.selectbox(
                    'dataset',
                      ('iris','breast Cancer','wine'))
classifier_name = st.sidebar.selectbox('Model',
                      ('Select Classifer',
                       'KNN','SVM','Random_Forest')                
                                      )
# import dataset

def get_dataset(dataset_name):
    if dataset_name == 'iris':
        data = datasets.load_iris()
    elif dataset_name == 'wine':
        data = datasets.load_wine()
    else: 
        data = datasets.load_breast_cancer()
    X = data.data
    y = data.target
    return X,y
# ab het_dataset lo call kr ly gye aur is ko X,y k equal ly gye
X,y = get_dataset(dataset_name)
st.write("Shape of Dataset",X.shape)
st.write("Unique Values",len(np.unique(y)))

# ab hum log model k parameter add karye gye
def add_parameter_ui(classifier_name):
    param = dict()
    if classifier_name =='SVM':
        C = st.sidebar.slider('C',0.01,10.0)                      
        param['C'] = C
    elif classifier_name =='KNN':
        K = st.sidebar.slider('K',1,15)
        param['K'] = K
    else:
        max_depth = st.sidebar.slider('max_depth',2,15)
        param['max_depth'] = max_depth  # jangle kitna guna hai
        n_estimators = st.sidebar.slider('n_estimators',1,100)
        param['n_estimators'] = n_estimators
    return param
    
    
params  = add_parameter_ui(classifier_name)
    
    # ab hum function ko call krye gye


# # ab hum machine learnig k model fitting karye gye

def get_classifier(classifier_name,params):
        clf = None
        if classifier_name == 'SVM':
            clf = SVC(C = params['C'])
        elif classifier_name == 'KNN':
            clf =KNeighborsClassifier(n_neighbors=params['K'])
        else:
            clf = clf=RandomForestClassifier(n_estimators=params['n_estimators'],                 
                           max_depth = params['max_depth'],random_state=1234) 
        return clf    
    
clf = get_classifier(classifier_name,params)

X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.20,random_state=0)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

acc = accuracy_score(y_test,y_pred) 
st.write(f'Classifier,{classifier_name}')
st.write(f'Accuracy,{acc}')